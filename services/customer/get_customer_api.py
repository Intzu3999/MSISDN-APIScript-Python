import os
import aiohttp
from utils import handle_api_error
from asyncio import Semaphore
from services.auth import get_access_token

MOLI_BASE_URL = os.getenv("MOLI_BASE_URL")

api_rate_limiter = Semaphore(5)

async def get_customer_api(msisdn):
    # async with api_rate_limiter: I commented this out to test the 429 http status being printed out or not
        result = {"msisdn": msisdn}
        
        try:
            token = await get_access_token()
        except Exception as error:
            print(f"❌ Failed to fetch token: {error}")
            return result  # Return empty result

        #THERE IS ANOTHER APPROAH: ISOLATE THE URL AND PARAMS AND PATH.
        # get_customer_params = {"msisdn": msisdn}
        # get_customer_url = f"{MOLI_BASE_URL}/moli-customer/v3/customer"
        # THEN, AT aiohttp.ClientSession() ADD: params=get_customer_params) as response:
        get_customer_url = f"{MOLI_BASE_URL}/moli-customer/v3/customer?msisdn={msisdn}"

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(
                    get_customer_url,
                    headers={
                        "Authorization": f"Bearer {token}",
                        "Content-Type": "application/json",
                    },
                ) as response:

                    response.raise_for_status()
                    data = await response.json()

                    id_no = data[0]["personalInfo"][0]["identification"][0].get("idNo", "N/A")
                    id_type = data[0]["personalInfo"][0]["identification"][0]["type"].get("code", "NA")
                    country_code = data[0]["contact"]["address"][0]["country"].get("code", "NA")

                    print(f"✅ get_customer_api: {response.status} {msisdn} id:{id_type} {id_no} countryCode:{country_code}")

                    result["getCustomerApiData"] = {
                        "customerStatus": f"✅ {response.status}",
                        "idType": id_type,
                        "idNo": id_no,
                        "countryCode": country_code,
                    }

        except aiohttp.ClientResponseError as error:
            return await handle_api_error(error, msisdn)

        except Exception as error:
            return await handle_api_error(error, msisdn)
        
        return result