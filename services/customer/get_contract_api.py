import os
import aiohttp
import urllib.parse
from utils.handle_api_error import handle_api_error
from asyncio import Semaphore
from services.auth import get_access_token

MOLI_BASE_URL = os.getenv("MOLI_BASE_URL")

service_rate_limiter = Semaphore(5)

async def get_contract_api(msisdn):
    async with service_rate_limiter:
        service = "get_contract_api"
        service_data = f"{service}_data"
        result = {"msisdn": msisdn}
        try:
            token = await get_access_token()
        except Exception as error:
            print(f"❌ Failed to fetch token: {error}")
            return result  # Return empty result

        get_contract_api_url = f"{MOLI_BASE_URL}/moli-customer/v1/customer/{msisdn}/contract"
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(
                    get_contract_api_url,
                    headers={
                        "Authorization": f"Bearer {token}",
                        "Content-Type": "application/json",
                    },
                ) as response:

                    response.raise_for_status()
                    data = await response.json()

                    # print("🛠️ get_contract_api Payload:", data)

                    contract_data = data if isinstance(data, dict) else {}

                    extracted_data = {
                        "msisdn": contract_data.get("msisdn", "N/A"),
                        "telco": contract_data.get("telco", "N/A"),
                        "productType": contract_data.get("productType", "N/A"),  
                        "productName": contract_data.get("productName", "N/A"), 
                        "startDate": contract_data.get("startDate", "N/A"),
                        "status": contract_data.get("status", "N/A"),
                    }

                    print(f"✅ get_contract_api: {response.status} {msisdn} {extracted_data['telco']} productType:{extracted_data['productType']} {extracted_data['productName']}")

                    result[service_data] = {
                        "customerStatus": f"✅ {response.status}",
                        **extracted_data,  # Expands dictionary to maintain consistency
                    }

        except aiohttp.ClientResponseError as error:
            return await handle_api_error(error, msisdn, service)

        except Exception as error:
            return await handle_api_error(error, msisdn, service)
        
        return result