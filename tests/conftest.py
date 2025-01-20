import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import app
from database import Base, get_db_connection
from repositories import ConversationRepository
from mock_repo import MockConversationRepository

# Create a new engine and session for testing
# SQLALCHEMY_TEST_DATABASE_URL = "sqlite:///./test.db"
# engine = create_engine(SQLALCHEMY_TEST_DATABASE_URL, connect_args={"check_same_thread": False})
# TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# # Create the test database tables
# Base.metadata.create_all(bind=engine)

# @pytest.fixture(scope="module")
# def test_db():
#     db = TestingSessionLocal()
    # Insert test data
    # conversation = Conversation(chat_id=2, message_counter=1, message_text="Test message")
    # db.add(conversation)
    # db.commit()
    # try:
    #     yield db
    # finally:
    #     db.close()

# @pytest.fixture(scope="module")
# def test_client(test_db):
#     def override_get_db():
#         try:
#             yield test_db
#         finally:
#             test_db.close()
@pytest.fixture(scope="module")
def test_client():
    app.dependency_overrides[ConversationRepository] = MockConversationRepository
    with TestClient(app) as client:
        yield client