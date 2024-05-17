from app import app
import os

port = os.environ.get('PORT')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port)
