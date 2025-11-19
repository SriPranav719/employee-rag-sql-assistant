import random
from .database import SessionLocal, Base, engine
from .models import Employee

def seed_data():
    Base.metadata.create_all(bind=engine)

    session = SessionLocal()
    try:
        if session.query(Employee).count() > 0:
            return

        departments = ["HR", "Finance", "IT", "Marketing", "Operations", "Sales"]
        batch = []

        for i in range(1, 201):
            batch.append(Employee(
                id=i,
                name=f"Employee {i}",
                email=f"user{i}@example.com",
                phone=f"987654{i:03d}",
                department=random.choice(departments),
                salary=round(random.uniform(20000, 150000), 2)
            ))

        session.bulk_save_objects(batch)
        session.commit()
        print("Seeded 200 employees.")
    finally:
        session.close()


if __name__ == "__main__":
    seed_data()
