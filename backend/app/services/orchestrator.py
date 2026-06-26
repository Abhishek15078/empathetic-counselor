import time

from app.core.dependencies import session_manager

from app.services.safety import SafetyService
from app.services.emotion import EmotionClassifier
from app.services.memory import (
    TrajectoryTracker
)
from app.services.rag import RAGService
from app.services.context import ContextBuilder
from app.services.llm import LLMCaller

from app.models.pipeline import PipelineResult


class AIOrchestrator:

    def __init__(self):

        self.safety = SafetyService()

        self.emotion_classifier = (
            EmotionClassifier()
        )

        # Shared SessionManager
        self.memory_manager = (
            session_manager
        )

        self.trajectory_tracker = (
            TrajectoryTracker()
        )

        self.rag_service = (
            RAGService()
        )

        self.context_builder = (
            ContextBuilder()
        )

        self.llm = (
            LLMCaller()
        )

    def process_message(
        self,
        session_id: str,
        user_message: str
    ) -> PipelineResult:

        start_time = time.time()

        # =====================================
        # STEP 1: SAFETY CHECK
        # =====================================

        safety_result = (
            self.safety.screen(
                user_message
            )
        )

        if safety_result.is_crisis:

            safe_response = (
                self.safety.load_safe_response()
            )

            end_time = time.time()

            return PipelineResult(
                response_text=safe_response,
                emotion_result=None,
                trajectory=None,
                rag_documents_used=[],
                safety_triggered=True,
                turn_number=0,
                processing_time_ms=int(
                    (end_time - start_time)
                    * 1000
                )
            )

        # =====================================
        # STEP 2: LOAD SESSION
        # =====================================

        session = (
            self.memory_manager.get_session(
                session_id
            )
        )

        # =====================================
        # STEP 3: EMOTION DETECTION
        # =====================================

        emotion_result = (
            self.emotion_classifier.classify(
                user_message
            )
        )

        # =====================================
        # STEP 4: SAVE EMOTION
        # =====================================

        session.add_emotion(
            emotion_result
        )

        # =====================================
        # STEP 5: TRAJECTORY ANALYSIS
        # =====================================

        trajectory = (
            self.trajectory_tracker.analyze(
                session.get_emotion_log()
            )
        )

        # =====================================
        # STEP 6: RAG RETRIEVAL
        # =====================================

        try:

            rag_chunks = (
                self.rag_service.retrieve(
                    user_message,
                    emotion_result.label.value
                )
            )

        except Exception:

            rag_chunks = []

        # =====================================
        # STEP 7: BUILD CONTEXT
        # =====================================

        messages = (
            self.context_builder.build(
                session,
                emotion_result,
                rag_chunks
            )
        )

        # =====================================
        # STEP 8: GENERATE RESPONSE
        # =====================================

        try:

            response = (
                self.llm.generate_from_messages(
                    messages
                )
            )

        except Exception as e:

            print("\n========== LLM ERROR ==========")
            print(e)
            print("===============================\n")

            response = (
                "I apologize, but I am having "
                "trouble generating a response "
                "right now. Please try again."
            )

        # =====================================
        # STEP 9: SAVE CONVERSATION
        # =====================================

        session.add_message(
            "user",
            user_message
        )

        session.add_message(
            "assistant",
            response
        )

        # =====================================
        # STEP 10: DOCUMENT LIST
        # =====================================

        rag_documents_used = []

        for doc, metadata in rag_chunks:

            if (
                isinstance(metadata, dict)
                and "source" in metadata
            ):

                rag_documents_used.append(
                    metadata["source"]
                )

        # =====================================
        # STEP 11: PROCESSING TIME
        # =====================================

        end_time = time.time()

        processing_time_ms = int(
            (end_time - start_time)
            * 1000
        )

        # =====================================
        # STEP 12: RETURN RESULT
        # =====================================

        return PipelineResult(
            response_text=response,
            emotion_result=emotion_result,
            trajectory=trajectory,
            rag_documents_used=rag_documents_used,
            safety_triggered=False,
            turn_number=len(
                session.messages
            ),
            processing_time_ms=processing_time_ms
        )