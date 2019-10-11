import boto3
from botocore.client import Config
from io import StringIO
from minio import Minio
from minio.error import ResponseError
import os

class MinioConnector:
    """ Implements the MinioConnector class """

    def write_dataframe_to_csv(self, filename, dataframe):
        """ Write dataframe to CSV to Minio """
        csv_buffer = StringIO()
        dataframe.to_csv(csv_buffer, index=False)
        self.s3_resource.Object('datalake', filename).put(Body=csv_buffer.getvalue())
        
    @property
    def minio_client(self): 
        """ Returns the Minio client """
        return Minio(
            os.environ.get("MINIO_SERVER"),
            access_key=os.environ.get("MINIO_ACCESS_KEY"),
            secret_key=os.environ.get("MINIO_SECRET_KEY"),
            secure=False
        )

    @property
    def s3_client(self):
        """ Returns the S3 client """
        return boto3.client('s3', 
            aws_access_key_id=os.environ.get("MINIO_ACCESS_KEY"),
            aws_secret_access_key=os.environ.get("MINIO_SECRET_KEY"),
            endpoint_url=f'http://{os.environ.get("MINIO_SERVER")}',
            config=Config(signature_version='s3v4')
        )

    @property
    def s3_resource(self):
        """ Returns the S3 resource """
        return boto3.resource('s3', 
            aws_access_key_id=os.environ.get("MINIO_ACCESS_KEY"),
            aws_secret_access_key=os.environ.get("MINIO_SECRET_KEY"),
            endpoint_url=f'http://{os.environ.get("MINIO_SERVER")}',
            config=Config(signature_version='s3v4')
        )
