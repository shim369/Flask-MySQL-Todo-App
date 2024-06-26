from extensions import db

class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer,primary_key=True)
    taskname = db.Column(db.String(80),nullable=False,unique=False)
    url = db.Column(db.String(200),nullable=False,unique=False)
    created_at = db.Column(db.DateTime(),nullable=False,server_default=db.func.now())
    updated_at = db.Column(db.DateTime(),nullable=False,server_default=db.func.now(),onupdate=db.func.now())

    @property
    def data(self):
        return {
            'id':self.id,
            'taskname':self.taskname,
            'url':self.url,
        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_all(cls):
        r = cls.query.all()
        result = []

        for i in r:
            result.append(i.data)
        return result
    
    @classmethod
    def get_by_id(cls,id):
        return cls.query.filter(cls.id == id).first()