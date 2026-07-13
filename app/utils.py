#purpose utility services (MinIO Storage and PDF Processing)
import boto3
from botocore.exceptions import ClientError
from app.config import settings
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
def get_s3_client():
    """creates and returns a Boto3 client configured for MinIO.
    """
    return boto3.client(
        's3',
        endpoint_url=settings.MINIO_ENDPOINT,
        aws_access_key_id=settings.MINIO_ACCESS_KEY,
        aws_secret_access_key=settings.MINIO_SECRET_KEY,
        config=boto3.session.Config(signature_version='s3v4')
    )
def init_storage():
    s3=get_s3_client()
    bucket_name = settings.MINIO_BUCKET
    try:
        #check if bucket exists by askig for its metadata (head)
        s3.head_bucket(Bucket=bucket_name)
        logger.info(f"Storage: Bucket '{bucket_name}' already exists")
    except ClientError:
        try:
            s3.create_bucket(Bucket=bucket_name)
            logger.info(f"Stroage: Bucket '{bucket_name} created successfully")
        except Exception as e:
            logger.info(f"Storage: Bucket '{bucket_name}' created successfully")