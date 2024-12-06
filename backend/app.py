from flask import Flask, request, jsonify
from telegram import Bot
import hashlib
import hmac
import os
from dotenv import load_dotenv
from flask_cors import CORS
import logging

load_dotenv()

# Logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# CORS configuration with environment variables
ALLOWED_ORIGINS = os.getenv('ALLOWED_ORIGINS', 'http://localhost:3000').split(',')
CORS(app, resources={
    r"/*": {
        "origins": ALLOWED_ORIGINS,
        "methods": ["POST", "OPTIONS"],
        "allow_headers": ["Content-Type"]
    }
})

BOT_TOKEN = os.getenv('BOT_TOKEN')

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN not set in environment variables")

bot = Bot(BOT_TOKEN)

def validate_init_data(init_data: str) -> bool:
    try:
        # Parsing the init_data string
        data_check_string = init_data.split('&')
        hash_value = next(item.split('=')[1] for item in data_check_string if item.startswith('hash='))
        
        # Removing hash from the data to be checked
        data_check_string = [item for item in data_check_string if not item.startswith('hash=')]
        data_check_string.sort()
        data_check_string = '\n'.join(data_check_string)
        
        # Calculating secret_key and hash
        secret_key = hmac.new(
            key=b"WebAppData",
            msg=BOT_TOKEN.encode(),
            digestmod=hashlib.sha256
        ).digest()
        
        calculated_hash = hmac.new(
            key=secret_key,
            msg=data_check_string.encode(),
            digestmod=hashlib.sha256
        ).hexdigest()
        
        return calculated_hash == hash_value
    except Exception as e:
        logger.error(f"Error validating init_data: {e}")
        return False

@app.route('/validate', methods=['POST'])
def validate():
    try:
        init_data = request.json.get('initData')
        
        if not init_data:
            logger.warning("Request received without initData")
            return jsonify({
                'error': 'initData is required',
                'status': 'error'
            }), 400
        
        is_valid = validate_init_data(init_data)
        
        if is_valid:
            logger.info("Successful validation of initData")
            return jsonify({
                'valid': True,
                'message': 'initData is valid',
                'status': 'success'
            })
        else:
            logger.warning("Invalid initData")
            return jsonify({
                'valid': False,
                'message': 'initData is invalid',
                'status': 'error'
            }), 400
            
    except Exception as e:
        logger.error(f"Uncaught error: {e}")
        return jsonify({
            'error': 'Internal server error',
            'status': 'error'
        }), 500

@app.errorhandler(404)
def not_found(e):
    return jsonify({
        'error': 'Route not found',
        'status': 'error'
    }), 404

@app.errorhandler(500)
def server_error(e):
    return jsonify({
        'error': 'Internal server error',
        'status': 'error'
    }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=os.getenv('FLASK_DEBUG', 'False').lower() == 'true')
