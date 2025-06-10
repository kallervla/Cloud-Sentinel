from logger import setup_logger
from alerts import send_alert
import boto3

logger = setup_logger()

def monitor_aws():
    logger.info("Starting AWS resource monitoring...")

    ec2 = boto3.client('ec2')
    instances = ec2.describe_instances()
    logger.info(f"Found {len(instances['Reservations'])} EC2 reservations.")

    # Dummy example of alert condition
    if not instances['Reservations']:
        send_alert("No EC2 instances found!")

if __name__ == "__main__":
    monitor_aws()

