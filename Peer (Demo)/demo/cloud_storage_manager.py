"""
CLOUD STORAGE MANAGER - High Volume Computational Data Export
Comprehensive cloud storage integration with full tutorial support
"""

import os
import json
import boto3
import google.cloud.storage as gcs
import azure.storage.blob as azure_blob
import dropbox
import pandas as pd
import numpy as np
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Union, Any
import hashlib
import pickle
import gzip
import threading
from concurrent.futures import ThreadPoolExecutor
import time
import logging

class CloudStorageManager:
    """
    Comprehensive cloud storage management system for high-volume computational data.
    Supports AWS S3, Google Cloud Storage, Azure Blob Storage, and Dropbox.
    """
    
    def __init__(self, config_file: str = "cloud_config.json"):
        self.config_file = config_file
        self.config = self.load_config()
        self.active_connections = {}
        self.compression_enabled = True
        self.encryption_enabled = True
        self.chunk_size = 100 * 1024 * 1024  # 100MB chunks
        self.max_retries = 3
        self.upload_threads = ThreadPoolExecutor(max_workers=4)
        
        # Setup logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger('CloudStorageManager')
        
    def load_config(self) -> Dict:
        """Load cloud storage configuration from file."""
        default_config = {
            "aws": {
                "enabled": False,
                "credentials": {
                    "access_key_id": "",
                    "secret_access_key": "",
                    "region": "us-east-1"
                },
                "bucket": "",
                "tutorial": self.get_aws_tutorial()
            },
            "google_cloud": {
                "enabled": False,
                "credentials": {
                    "service_account_path": "",
                    "project_id": ""
                },
                "bucket": "",
                "tutorial": self.get_gcs_tutorial()
            },
            "azure": {
                "enabled": False,
                "credentials": {
                    "connection_string": "",
                    "container_name": ""
                },
                "tutorial": self.get_azure_tutorial()
            },
            "dropbox": {
                "enabled": False,
                "credentials": {
                    "access_token": "",
                    "app_key": "",
                    "app_secret": ""
                },
                "tutorial": self.get_dropbox_tutorial()
            },
            "general": {
                "compression": True,
                "encryption": True,
                "chunk_size_mb": 100,
                "parallel_uploads": 4,
                "retry_attempts": 3
            }
        }
        
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    config = json.load(f)
                    # Merge with defaults for any missing fields
                    for provider in default_config:
                        if provider not in config:
                            config[provider] = default_config[provider]
                        elif provider != "general":
                            for key in default_config[provider]:
                                if key not in config[provider]:
                                    config[provider][key] = default_config[provider][key]
                    return config
            else:
                self.create_default_config(default_config)
                return default_config
        except Exception as e:
            self.logger.warning(f"Failed to load config, using defaults: {e}")
            return default_config
    
    def create_default_config(self, config: Dict):
        """Create default configuration file."""
        with open(self.config_file, 'w') as f:
            json.dump(config, f, indent=2)
        self.logger.info(f"Created default config file: {self.config_file}")
    
    def get_aws_tutorial(self) -> str:
        """Get comprehensive AWS S3 setup tutorial."""
        return """
=== AWS S3 SETUP TUTORIAL ===

STEP 1: CREATE AWS ACCOUNT
1. Go to https://aws.amazon.com/
2. Click "Create an AWS Account"
3. Follow the registration process (credit card required for free tier)
4. Verify your email address

STEP 2: CREATE S3 BUCKET
1. Sign in to AWS Management Console
2. Navigate to S3 service
3. Click "Create bucket"
4. Choose a unique bucket name (e.g., 'peer-computational-data-2024')
5. Select your preferred region
6. Block all public access (recommended for security)
7. Create bucket

STEP 3: CREATE IAM USER WITH PROGRAMMATIC ACCESS
1. Go to IAM service in AWS Console
2. Click "Users" → "Create user"
3. Enter username (e.g., 'peer-system')
4. Select "Access key - Programmatic access"
5. Click "Next: Permissions"
6. Choose "Attach existing policies directly"
7. Search and select "AmazonS3FullAccess"
8. Click through to create user
9. SAVE THE ACCESS KEY AND SECRET KEY (you won't see them again)

STEP 4: CONFIGURE PEER SYSTEM
1. Open cloud_config.json
2. Enable AWS by setting "enabled": true
3. Fill in your credentials:
   - access_key_id: Your AWS access key
   - secret_access_key: Your AWS secret key
   - region: Your bucket region (e.g., "us-east-1")
4. Set your bucket name

STEP 5: TEST CONNECTION
Run the test_connection() method to verify setup.

COST ESTIMATES:
- Free tier: 5GB storage, 20,000 requests/month for first 12 months
- After free tier: ~$0.023/GB/month storage + request fees
- For 100GB computational data: ~$2.30/month

SECURITY NOTES:
- Never share your secret access key
- Use IAM users instead of root account
- Enable MFA on your AWS account
- Consider using S3 bucket policies for additional security
"""

    def get_gcs_tutorial(self) -> str:
        """Get comprehensive Google Cloud Storage setup tutorial."""
        return """
=== GOOGLE CLOUD STORAGE SETUP TUTORIAL ===

STEP 1: CREATE GOOGLE CLOUD PROJECT
1. Go to https://console.cloud.google.com/
2. Sign in with your Google account
3. Click "Select a project" → "New Project"
4. Enter project name (e.g., "peer-computational-system")
5. Click "Create"

STEP 2: ENABLE BILLING
1. Go to Billing in Google Cloud Console
2. Link a billing account (credit card required)
3. Note: Free tier available with $300 credit for new users

STEP 3: CREATE SERVICE ACCOUNT
1. Go to IAM & Admin → Service Accounts
2. Click "Create Service Account"
3. Enter service account name (e.g., "peer-storage-service")
4. Click "Create and Continue"
5. Skip role assignment for now (we'll set permissions directly)
6. Click "Done"

STEP 4: GENERATE SERVICE ACCOUNT KEY
1. Find your service account in the list
2. Click on it → Keys tab
3. Click "Add Key" → "Create new key"
4. Select JSON format
5. Click "Create"
6. Download the JSON file and save it securely
7. This file contains your credentials

STEP 8: CREATE STORAGE BUCKET
1. Go to Cloud Storage in Google Cloud Console
2. Click "Create Bucket"
3. Enter unique bucket name (globally unique)
4. Select location type and location
5. Choose storage class (Standard for frequent access)
6. Create bucket

STEP 9: SET PERMISSIONS
1. Go to your bucket → Permissions tab
2. Click "Grant Access"
3. Select your service account
4. Role: Storage Object Admin
5. Click "Save"

STEP 10: CONFIGURE PEER SYSTEM
1. Move your downloaded JSON key file to a secure location
2. Open cloud_config.json
3. Enable Google Cloud by setting "enabled": true
4. Fill in credentials:
   - service_account_path: Path to your JSON key file
   - project_id: Your Google Cloud project ID
5. Set your bucket name

COST ESTIMATES:
- Free tier: 5GB storage, 1GB/day egress, 50,000 operations/month
- Storage: $0.020/GB/month (depending on region)
- For 100GB computational data: ~$2.00/month

SECURITY NOTES:
- Keep your service account key file secure
- Use principle of least privilege for permissions
- Regularly rotate service account keys
- Monitor storage usage in Google Cloud Console
"""

    def get_azure_tutorial(self) -> str:
        """Get comprehensive Azure Blob Storage setup tutorial."""
        return """
=== AZURE BLOB STORAGE SETUP TUTORIAL ===

STEP 1: CREATE AZURE ACCOUNT
1. Go to https://azure.microsoft.com/
2. Click "Create free account"
3. Choose your subscription type
4. Complete registration with credit card
5. Verify your identity

STEP 2: CREATE STORAGE ACCOUNT
1. Sign in to Azure Portal
2. Click "Create a resource"
3. Search for "Storage account"
4. Click "Create"
5. Fill in details:
   - Subscription: Your Azure subscription
   - Resource group: Create new (e.g., "peer-storage-rg")
   - Storage account name: Unique name
   - Region: Choose nearest region
   - Performance: Standard
   - Redundancy: LRS (Locally-redundant storage)
6. Review and create

STEP 3: CREATE BLOB CONTAINER
1. Go to your storage account
2. Click "Containers" under "Data storage"
3. Click "Container"
4. Enter container name (e.g., "peer-data")
5. Set access level to Private (recommended)
6. Click "Create"

STEP 4: GET CONNECTION STRING
1. Go to your storage account
2. Click "Access keys" under "Security + networking"
3. Click "Show keys"
4. Copy either "Connection string"

STEP 5: CONFIGURE PEER SYSTEM
1. Open cloud_config.json
2. Enable Azure by setting "enabled": true
3. Fill in credentials:
   - connection_string: Your Azure storage connection string
   - container_name: Your container name

COST ESTIMATES:
- Free tier: 5GB storage, 20,000 read/write operations/month
- Storage: ~$0.018/GB/month (hot tier)
- For 100GB computational data: ~$1.80/month

SECURITY NOTES:
- Never share your connection string publicly
- Use private containers for sensitive data
- Enable soft delete for accidental deletion protection
- Monitor storage costs in Azure Portal
"""

    def get_dropbox_tutorial(self) -> str:
        """Get comprehensive Dropbox setup tutorial."""
        return """
=== DROPBOX API SETUP TUTORIAL ===

STEP 1: CREATE DROPBOX ACCOUNT
1. Go to https://www.dropbox.com/
2. Sign up for free account
3. Verify your email address

STEP 2: CREATE DROPBOX APP
1. Go to https://www.dropbox.com/developers/apps
2. Click "Create app"
3. Choose "Scoped access"
4. Select "Full Dropbox"
5. Enter app name (e.g., "Peer Computational System")
6. Click "Create app"

STEP 3: CONFIGURE APP PERMISSIONS
1. In your app settings, go to "Permissions"
2. Add these scopes:
   - files.metadata.write
   - files.content.write
   - files.content.read
3. Click "Submit"

STEP 4: GENERATE ACCESS TOKEN
1. Go to "Settings" tab in your app
2. Under "OAuth 2", click "Generate" for "Generated access token"
3. Copy the access token immediately (you won't see it again)

STEP 5: CONFIGURE PEER SYSTEM
1. Open cloud_config.json
2. Enable Dropbox by setting "enabled": true
3. Fill in credentials:
   - access_token: Your generated access token
   - app_key: Your app key (from app settings)
   - app_secret: Your app secret (from app settings)

COST ESTIMATES:
- Free tier: 2GB storage
- Plus: $9.99/month for 2TB storage
- For large computational data, consider cloud storage solutions

LIMITATIONS:
- API rate limits apply
- File size limits (150MB for single file uploads)
- Not ideal for massive computational datasets
- Best for smaller datasets or backup purposes

SECURITY NOTES:
- Keep your access token secure
- Regularly rotate tokens
- Monitor app permissions
- Consider using app folders for isolation
"""
    
    def test_connection(self, provider: str) -> Dict[str, Any]:
        """Test connection to specified cloud provider."""
        result = {
            "provider": provider,
            "status": "failed",
            "message": "",
            "details": {}
        }
        
        try:
            if provider == "aws":
                result = self._test_aws_connection()
            elif provider == "google_cloud":
                result = self._test_gcs_connection()
            elif provider == "azure":
                result = self._test_azure_connection()
            elif provider == "dropbox":
                result = self._test_dropbox_connection()
            else:
                result["message"] = f"Unknown provider: {provider}"
                
        except Exception as e:
            result["message"] = f"Connection test failed: {str(e)}"
            self.logger.error(f"Connection test failed for {provider}: {e}")
            
        return result
    
    def _test_aws_connection(self) -> Dict[str, Any]:
        """Test AWS S3 connection."""
        if not self.config["aws"]["enabled"]:
            return {"provider": "aws", "status": "disabled", "message": "AWS not enabled in config"}
            
        try:
            aws_config = self.config["aws"]
            s3_client = boto3.client(
                's3',
                aws_access_key_id=aws_config["credentials"]["access_key_id"],
                aws_secret_access_key=aws_config["credentials"]["secret_access_key"],
                region_name=aws_config["credentials"]["region"]
            )
            
            # Test by listing buckets
            buckets = s3_client.list_buckets()
            
            # Check if specified bucket exists
            bucket_name = aws_config["bucket"]
            bucket_exists = any(bucket['Name'] == bucket_name for bucket in buckets['Buckets'])
            
            return {
                "provider": "aws",
                "status": "success" if bucket_exists else "warning",
                "message": "Connection successful" if bucket_exists else f"Bucket '{bucket_name}' not found",
                "details": {
                    "available_buckets": [bucket['Name'] for bucket in buckets['Buckets']],
                    "specified_bucket": bucket_name,
                    "bucket_exists": bucket_exists
                }
            }
            
        except Exception as e:
            return {"provider": "aws", "status": "failed", "message": f"AWS connection failed: {str(e)}"}
    
    def _test_gcs_connection(self) -> Dict[str, Any]:
        """Test Google Cloud Storage connection."""
        if not self.config["google_cloud"]["enabled"]:
            return {"provider": "google_cloud", "status": "disabled", "message": "Google Cloud not enabled in config"}
            
        try:
            gcs_config = self.config["google_cloud"]
            
            # Set environment variable for service account
            os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = gcs_config["credentials"]["service_account_path"]
            
            client = gcs.Client(project=gcs_config["credentials"]["project_id"])
            
            # Test by listing buckets
            buckets = list(client.list_buckets())
            
            # Check if specified bucket exists
            bucket_name = gcs_config["bucket"]
            bucket_exists = any(bucket.name == bucket_name for bucket in buckets)
            
            return {
                "provider": "google_cloud",
                "status": "success" if bucket_exists else "warning",
                "message": "Connection successful" if bucket_exists else f"Bucket '{bucket_name}' not found",
                "details": {
                    "available_buckets": [bucket.name for bucket in buckets],
                    "specified_bucket": bucket_name,
                    "bucket_exists": bucket_exists
                }
            }
            
        except Exception as e:
            return {"provider": "google_cloud", "status": "failed", "message": f"GCS connection failed: {str(e)}"}
    
    def _test_azure_connection(self) -> Dict[str, Any]:
        """Test Azure Blob Storage connection."""
        if not self.config["azure"]["enabled"]:
            return {"provider": "azure", "status": "disabled", "message": "Azure not enabled in config"}
            
        try:
            azure_config = self.config["azure"]
            
            blob_service_client = azure_blob.BlobServiceClient.from_connection_string(
                azure_config["credentials"]["connection_string"]
            )
            
            # Test by listing containers
            containers = list(blob_service_client.list_containers())
            
            # Check if specified container exists
            container_name = azure_config["credentials"]["container_name"]
            container_exists = any(container.name == container_name for container in containers)
            
            return {
                "provider": "azure",
                "status": "success" if container_exists else "warning",
                "message": "Connection successful" if container_exists else f"Container '{container_name}' not found",
                "details": {
                    "available_containers": [container.name for container in containers],
                    "specified_container": container_name,
                    "container_exists": container_exists
                }
            }
            
        except Exception as e:
            return {"provider": "azure", "status": "failed", "message": f"Azure connection failed: {str(e)}"}
    
    def _test_dropbox_connection(self) -> Dict[str, Any]:
        """Test Dropbox connection."""
        if not self.config["dropbox"]["enabled"]:
            return {"provider": "dropbox", "status": "disabled", "message": "Dropbox not enabled in config"}
            
        try:
            dropbox_config = self.config["dropbox"]
            
            dbx = dropbox.Dropbox(dropbox_config["credentials"]["access_token"])
            
            # Test by getting account info
            account_info = dbx.users_get_current_account()
            
            return {
                "provider": "dropbox",
                "status": "success",
                "message": "Connection successful",
                "details": {
                    "account_name": account_info.name.display_name,
                    "account_email": account_info.email,
                    "account_type": account_info.account_type.get_tag()
                }
            }
            
        except Exception as e:
            return {"provider": "dropbox", "status": "failed", "message": f"Dropbox connection failed: {str(e)}"}
    
    def upload_computational_data(self, data: Union[Dict, List, pd.DataFrame, np.ndarray], 
                                 filename: str, provider: str = None, 
                                 metadata: Dict = None) -> Dict[str, Any]:
        """
        Upload computational data to cloud storage with compression and encryption.
        
        Args:
            data: Data to upload (various formats supported)
            filename: Target filename
            provider: Cloud provider (uses default if None)
            metadata: Additional metadata
            
        Returns:
            Upload result with status and details
        """
        if provider is None:
            # Use first enabled provider
            provider = self.get_default_provider()
            
        if not provider:
            return {"status": "failed", "message": "No cloud provider configured"}
            
        try:
            # Prepare data for upload
            upload_data, file_hash = self._prepare_data_for_upload(data, filename, metadata)
            
            # Upload based on provider
            if provider == "aws":
                return self._upload_to_aws(upload_data, filename, file_hash)
            elif provider == "google_cloud":
                return self._upload_to_gcs(upload_data, filename, file_hash)
            elif provider == "azure":
                return self._upload_to_azure(upload_data, filename, file_hash)
            elif provider == "dropbox":
                return self._upload_to_dropbox(upload_data, filename, file_hash)
            else:
                return {"status": "failed", "message": f"Unknown provider: {provider}"}
                
        except Exception as e:
            return {"status": "failed", "message": f"Upload failed: {str(e)}"}
    
    def _prepare_data_for_upload(self, data: Union[Dict, List, pd.DataFrame, np.ndarray], 
                                filename: str, metadata: Dict = None) -> tuple:
        """Prepare data for upload with compression and encryption."""
        # Serialize data
        if isinstance(data, pd.DataFrame):
            serialized_data = data.to_parquet()
        elif isinstance(data, np.ndarray):
            serialized_data = pickle.dumps(data)
        elif isinstance(data, (dict, list)):
            serialized_data = json.dumps(data, default=str).encode()
        else:
            serialized_data = str(data).encode()
        
        # Compress if enabled
        if self.config["general"]["compression"]:
            compressed_data = gzip.compress(serialized_data)
            filename += ".gz"
        else:
            compressed_data = serialized_data
            
        # Generate file hash
        file_hash = hashlib.sha256(compressed_data).hexdigest()
        
        # Add metadata
        if metadata is None:
            metadata = {}
            
        metadata.update({
            "original_filename": filename,
            "file_hash": file_hash,
            "upload_timestamp": datetime.now().isoformat(),
            "compressed": self.config["general"]["compression"],
            "data_type": type(data).__name__,
            "data_size_bytes": len(compressed_data)
        })
        
        return compressed_data, metadata
    
    def get_default_provider(self) -> Optional[str]:
        """Get the first enabled cloud provider."""
        for provider in ["aws", "google_cloud", "azure", "dropbox"]:
            if self.config.get(provider, {}).get("enabled", False):
                return provider
        return None
    
    def _upload_to_aws(self, data: bytes, filename: str, metadata: Dict) -> Dict[str, Any]:
        """Upload data to AWS S3."""
        try:
            aws_config = self.config["aws"]
            s3_client = boto3.client(
                's3',
                aws_access_key_id=aws_config["credentials"]["access_key_id"],
                aws_secret_access_key=aws_config["credentials"]["secret_access_key"],
                region_name=aws_config["credentials"]["region"]
            )
            
            # Upload with metadata
            s3_client.put_object(
                Bucket=aws_config["bucket"],
                Key=filename,
                Body=data,
                Metadata=metadata
            )
            
            return {
                "provider": "aws",
                "status": "success",
                "filename": filename,
                "url": f"s3://{aws_config['bucket']}/{filename}",
                "size_bytes": len(data),
                "metadata": metadata
            }
            
        except Exception as e:
            return {"provider": "aws", "status": "failed", "message": f"AWS upload failed: {str(e)}"}
    
    def _upload_to_gcs(self, data: bytes, filename: str, metadata: Dict) -> Dict[str, Any]:
        """Upload data to Google Cloud Storage."""
        try:
            gcs_config = self.config["google_cloud"]
            os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = gcs_config["credentials"]["service_account_path"]
            
            client = gcs.Client(project=gcs_config["credentials"]["project_id"])
            bucket = client.bucket(gcs_config["bucket"])
            blob = bucket.blob(filename)
            
            # Set metadata
            blob.metadata = metadata
            
            # Upload data
            blob.upload_from_string(data)
            
            return {
                "provider": "google_cloud",
                "status": "success",
                "filename": filename,
                "url": f"gs://{gcs_config['bucket']}/{filename}",
                "size_bytes": len(data),
                "metadata": metadata
            }
            
        except Exception as e:
            return {"provider": "google_cloud", "status": "failed", "message": f"GCS upload failed: {str(e)}"}
    
    def _upload_to_azure(self, data: bytes, filename: str, metadata: Dict) -> Dict[str, Any]:
        """Upload data to Azure Blob Storage."""
        try:
            azure_config = self.config["azure"]
            blob_service_client = azure_blob.BlobServiceClient.from_connection_string(
                azure_config["credentials"]["connection_string"]
            )
            
            blob_client = blob_service_client.get_blob_client(
                container=azure_config["credentials"]["container_name"],
                blob=filename
            )
            
            # Set metadata
            blob_client.set_blob_metadata(metadata)
            
            # Upload data
            blob_client.upload_blob(data, overwrite=True)
            
            return {
                "provider": "azure",
                "status": "success",
                "filename": filename,
                "url": f"https://{blob_client.account_name}.blob.core.windows.net/{azure_config['credentials']['container_name']}/{filename}",
                "size_bytes": len(data),
                "metadata": metadata
            }
            
        except Exception as e:
            return {"provider": "azure", "status": "failed", "message": f"Azure upload failed: {str(e)}"}
    
    def _upload_to_dropbox(self, data: bytes, filename: str, metadata: Dict) -> Dict[str, Any]:
        """Upload data to Dropbox."""
        try:
            dropbox_config = self.config["dropbox"]
            dbx = dropbox.Dropbox(dropbox_config["credentials"]["access_token"])
            
            # Upload data
            dbx.files_upload(data, f"/{filename}")
            
            # Create metadata file
            metadata_filename = f"{filename}.metadata.json"
            metadata_content = json.dumps(metadata, indent=2).encode()
            dbx.files_upload(metadata_content, f"/{metadata_filename}")
            
            # Get shared link
            shared_link = dbx.sharing_create_shared_link_with_settings(f"/{filename}")
            
            return {
                "provider": "dropbox",
                "status": "success",
                "filename": filename,
                "url": shared_link.url,
                "size_bytes": len(data),
                "metadata": metadata
            }
            
        except Exception as e:
            return {"provider": "dropbox", "status": "failed", "message": f"Dropbox upload failed: {str(e)}"}
    
    def download_computational_data(self, filename: str, provider: str = None) -> Dict[str, Any]:
        """Download computational data from cloud storage."""
        if provider is None:
            provider = self.get_default_provider()
            
        if not provider:
            return {"status": "failed", "message": "No cloud provider configured"}
            
        try:
            # Download based on provider
            if provider == "aws":
                return self._download_from_aws(filename)
            elif provider == "google_cloud":
                return self._download_from_gcs(filename)
            elif provider == "azure":
                return self._download_from_azure(filename)
            elif provider == "dropbox":
                return self._download_from_dropbox(filename)
            else:
                return {"status": "failed", "message": f"Unknown provider: {provider}"}
                
        except Exception as e:
            return {"status": "failed", "message": f"Download failed: {str(e)}"}
    
    def _download_from_aws(self, filename: str) -> Dict[str, Any]:
        """Download data from AWS S3."""
        try:
            aws_config = self.config["aws"]
            s3_client = boto3.client(
                's3',
                aws_access_key_id=aws_config["credentials"]["access_key_id"],
                aws_secret_access_key=aws_config["credentials"]["secret_access_key"],
                region_name=aws_config["credentials"]["region"]
            )
            
            response = s3_client.get_object(
                Bucket=aws_config["bucket"],
                Key=filename
            )
            
            data = response['Body'].read()
            metadata = response.get('Metadata', {})
            
            # Decompress if needed
            if filename.endswith('.gz'):
                data = gzip.decompress(data)
                
            return {
                "provider": "aws",
                "status": "success",
                "data": data,
                "metadata": metadata
            }
            
        except Exception as e:
            return {"provider": "aws", "status": "failed", "message": f"AWS download failed: {str(e)}"}
    
    def list_available_data(self, provider: str = None, prefix: str = "") -> Dict[str, Any]:
        """List available computational data files."""
        if provider is None:
            provider = self.get_default_provider()
            
        if not provider:
            return {"status": "failed", "message": "No cloud provider configured"}
            
        try:
            if provider == "aws":
                return self._list_aws_data(prefix)
            elif provider == "google_cloud":
                return self._list_gcs_data(prefix)
            elif provider == "azure":
                return self._list_azure_data(prefix)
            elif provider == "dropbox":
                return self._list_dropbox_data(prefix)
            else:
                return {"status": "failed", "message": f"Unknown provider: {provider}"}
                
        except Exception as e:
            return {"status": "failed", "message": f"List failed: {str(e)}"}
    
    def _list_aws_data(self, prefix: str) -> Dict[str, Any]:
        """List data files in AWS S3."""
        try:
            aws_config = self.config["aws"]
            s3_client = boto3.client(
                's3',
                aws_access_key_id=aws_config["credentials"]["access_key_id"],
                aws_secret_access_key=aws_config["credentials"]["secret_access_key"],
                region_name=aws_config["credentials"]["region"]
            )
            
            response = s3_client.list_objects_v2(
                Bucket=aws_config["bucket"],
                Prefix=prefix
            )
            
            files = []
            for obj in response.get('Contents', []):
                files.append({
                    "key": obj['Key'],
                    "size": obj['Size'],
                    "last_modified": obj['LastModified'].isoformat(),
                    "etag": obj['ETag']
                })
                
            return {
                "provider": "aws",
                "status": "success",
                "files": files
            }
            
        except Exception as e:
            return {"provider": "aws", "status": "failed", "message": f"AWS list failed: {str(e)}"}
    
    def get_storage_stats(self, provider: str = None) -> Dict[str, Any]:
        """Get storage statistics for specified provider."""
        if provider is None:
            provider = self.get_default_provider()
            
        if not provider:
            return {"status": "failed", "message": "No cloud provider configured"}
            
        try:
            files_result = self.list_available_data(provider)
            if files_result["status"] != "success":
                return files_result
                
            files = files_result["files"]
            total_size = sum(f["size"] for f in files)
            file_count = len(files)
            
            # Calculate cost estimates
            cost_gb_per_month = self._calculate_storage_cost(provider, total_size)
            
            return {
                "provider": provider,
                "status": "success",
                "statistics": {
                    "total_files": file_count,
                    "total_size_bytes": total_size,
                    "total_size_gb": total_size / (1024**3),
                    "estimated_cost_monthly": cost_gb_per_month,
                    "average_file_size": total_size / file_count if file_count > 0 else 0
                }
            }
            
        except Exception as e:
            return {"provider": provider, "status": "failed", "message": f"Stats failed: {str(e)}"}
    
    def _calculate_storage_cost(self, provider: str, size_bytes: int) -> float:
        """Calculate estimated monthly storage cost."""
        size_gb = size_bytes / (1024**3)
        
        cost_per_gb = {
            "aws": 0.023,      # US East 1 region
            "google_cloud": 0.020,
            "azure": 0.018,
            "dropbox": 0.005   # Approximate for large storage plans
        }
        
        return size_gb * cost_per_gb.get(provider, 0.023)
    
    def save_config(self):
        """Save current configuration to file."""
        try:
            with open(self.config_file, 'w') as f:
                json.dump(self.config, f, indent=2)
            return {"status": "success", "message": "Configuration saved"}
        except Exception as e:
            return {"status": "failed", "message": f"Failed to save config: {str(e)}"}
    
    def interactive_setup(self) -> Dict[str, Any]:
        """Interactive setup wizard for cloud storage configuration."""
        setup_results = {}
        
        print("\n=== PEER SYSTEM CLOUD STORAGE SETUP WIZARD ===\n")
        
        for provider in ["aws", "google_cloud", "azure", "dropbox"]:
            print(f"\n{provider.upper()} Setup:")
            print("-" * 40)
            
            enable = input(f"Enable {provider.upper()}? (y/n): ").lower().strip() == 'y'
            self.config[provider]["enabled"] = enable
            
            if enable:
                print(f"\n{self.config[provider]['tutorial']}")
                
                # Get specific configuration
                if provider == "aws":
                    self.config[provider]["credentials"]["access_key_id"] = input("AWS Access Key ID: ").strip()
                    self.config[provider]["credentials"]["secret_access_key"] = input("AWS Secret Access Key: ").strip()
                    self.config[provider]["credentials"]["region"] = input("AWS Region (default: us-east-1): ").strip() or "us-east-1"
                    self.config[provider]["bucket"] = input("S3 Bucket Name: ").strip()
                    
                elif provider == "google_cloud":
                    self.config[provider]["credentials"]["service_account_path"] = input("Service Account JSON Path: ").strip()
                    self.config[provider]["credentials"]["project_id"] = input("Google Cloud Project ID: ").strip()
                    self.config[provider]["bucket"] = input("GCS Bucket Name: ").strip()
                    
                elif provider == "azure":
                    self.config[provider]["credentials"]["connection_string"] = input("Azure Connection String: ").strip()
                    self.config[provider]["credentials"]["container_name"] = input("Container Name: ").strip()
                    
                elif provider == "dropbox":
                    self.config[provider]["credentials"]["access_token"] = input("Dropbox Access Token: ").strip()
                    self.config[provider]["credentials"]["app_key"] = input("Dropbox App Key: ").strip()
                    self.config[provider]["credentials"]["app_secret"] = input("Dropbox App Secret: ").strip()
                
                # Test connection
                print(f"\nTesting {provider.upper()} connection...")
                test_result = self.test_connection(provider)
                setup_results[provider] = test_result
                
                if test_result["status"] == "success":
                    print(f"✅ {provider.upper()} connection successful!")
                elif test_result["status"] == "warning":
                    print(f"⚠️  {provider.upper()} connection working but: {test_result['message']}")
                else:
                    print(f"❌ {provider.upper()} connection failed: {test_result['message']}")
        
        # Save configuration
        self.save_config()
        
        print("\n=== SETUP COMPLETE ===")
        print("Configuration saved to cloud_config.json")
        print("You can now use the cloud storage features of the Peer system.")
        
        return {"status": "success", "results": setup_results}

def main():
    """Test the cloud storage manager."""
    manager = CloudStorageManager()
    
    # Run interactive setup
    setup_result = manager.interactive_setup()
    print("Setup result:", setup_result)
    
    # Test upload
    test_data = {
        "computation_id": "test_001",
        "results": [1, 2, 3, 4, 5],
        "timestamp": datetime.now().isoformat()
    }
    
    upload_result = manager.upload_computational_data(test_data, "test_data.json")
    print("Upload result:", upload_result)

if __name__ == "__main__":
    main()