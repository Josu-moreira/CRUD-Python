import mysql.connector as mysql
from contextlib import contextmanager


@contextmanager
def connection():
    try:
        db = mysql.connect(
            host="localhost",
            user="root",
            password="",
            database="",
        )

        try:
            yield db
            db.commit()

        except Exception:
            db.rollback()
            raise

        finally:
            db.close()

    except Exception as e:
        print(f"Connection Error: {e}")
