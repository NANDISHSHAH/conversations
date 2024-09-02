class ConversationRepository:
    db: Session

    def __init__(
            self, db: Session = Depends(get_db_connection)
    ) -> None:
        self.db = db

    def get(self, id):
        return self.db.get('conversations', id)

    def save(self, conversation):
        self.db.save('conversations', conversation)

    def delete(self, conversation):
        self.db.delete('conversations', conversation)
