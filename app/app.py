import os
import logging
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

from azure.monitor.opentelemetry import configure_azure_monitor

# Configure Azure Monitor OpenTelemetry
# It will automatically pick up the APPLICATIONINSIGHTS_CONNECTION_STRING from the environment
configure_azure_monitor(
    connection_string=os.environ.get("APPLICATIONINSIGHTS_CONNECTION_STRING"),
    enable_live_metrics=True
)

# Import Flask AFTER Azure Monitor is configured so the SDK can monkey-patch it!
from flask import Flask, request

app = Flask(__name__)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

@app.route("/")
def index():
    logger.info("Processed a request for the index page.")
    return "Azure Monitor Observability App is running!", 200

@app.route("/error")
def trigger_error():
    logger.error("A critical error was triggered!")
    try:
        1 / 0
    except ZeroDivisionError as e:
        logger.exception("Caught an exception, but returning a 500 error.")
        return "Internal Server Error Simulation", 500

@app.route("/cpu-stress")
def cpu_stress():
    logger.warning("CPU stress endpoint was called!")
    # Artificial loop to generate load
    x = 0
    for i in range(10000000):
        x += i
    return f"CPU stress complete. Result: {x}", 200

if __name__ == "__main__":
    # Ensure connection string is present
    if not os.environ.get("APPLICATIONINSIGHTS_CONNECTION_STRING"):
        print("WARNING: APPLICATIONINSIGHTS_CONNECTION_STRING is not set.")
    
    app.run(host="0.0.0.0", port=8080)
