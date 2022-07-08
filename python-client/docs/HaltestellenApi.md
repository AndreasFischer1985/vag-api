# vag.HaltestellenApi

All URIs are relative to *https://start.vag.de/dm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**haltestellen_get_by_location**](HaltestellenApi.md#haltestellen_get_by_location) | **GET** /api/v1/haltestellen/{netvu}/location | Liefert die Liste mit den Haltestellen zu der Umkreissuche
[**haltestellen_get_by_name**](HaltestellenApi.md#haltestellen_get_by_name) | **GET** /api/v1/haltestellen/{netvu} | Liefert die Liste mit den Haltestellen zu dem angegebenen Haltestellenname (Optional)


# **haltestellen_get_by_location**
> HaltestellenAPIResponse haltestellen_get_by_location(netvu, lon, lat)

Liefert die Liste mit den Haltestellen zu der Umkreissuche

### Example


```python
import time
from deutschland import vag
from deutschland.vag.api import haltestellen_api
from deutschland.vag.model.haltestellen_api_response import HaltestellenAPIResponse
from pprint import pprint
# Defining the host is optional and defaults to https://start.vag.de/dm
# See configuration.py for a list of all supported configuration parameters.
configuration = vag.Configuration(
    host = "https://start.vag.de/dm"
)


# Enter a context with an instance of the API client
with vag.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = haltestellen_api.HaltestellenApi(api_client)
    netvu = "netvu_example" # str | Netz des Verkehrsunternehmen, aktuell \"VAG\" oder \"VGN\"
    lon = 3.14 # float | Longitude für die Umkreissuche in WGS 84 Format in Grad
    lat = 3.14 # float | Latitude für die Umkreissuche in WGS 84 Format in Grad
    radius = 1 # int | Radius für die Umkreissuche. Defaultwert = 1000 Meter. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Liefert die Liste mit den Haltestellen zu der Umkreissuche
        api_response = api_instance.haltestellen_get_by_location(netvu, lon, lat)
        pprint(api_response)
    except vag.ApiException as e:
        print("Exception when calling HaltestellenApi->haltestellen_get_by_location: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Liefert die Liste mit den Haltestellen zu der Umkreissuche
        api_response = api_instance.haltestellen_get_by_location(netvu, lon, lat, radius=radius)
        pprint(api_response)
    except vag.ApiException as e:
        print("Exception when calling HaltestellenApi->haltestellen_get_by_location: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **netvu** | **str**| Netz des Verkehrsunternehmen, aktuell \&quot;VAG\&quot; oder \&quot;VGN\&quot; |
 **lon** | **float**| Longitude für die Umkreissuche in WGS 84 Format in Grad |
 **lat** | **float**| Latitude für die Umkreissuche in WGS 84 Format in Grad |
 **radius** | **int**| Radius für die Umkreissuche. Defaultwert &#x3D; 1000 Meter. | [optional]

### Return type

[**HaltestellenAPIResponse**](HaltestellenAPIResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **haltestellen_get_by_name**
> HaltestellenAPIResponse haltestellen_get_by_name(netvu, name)

Liefert die Liste mit den Haltestellen zu dem angegebenen Haltestellenname (Optional)

### Example


```python
import time
from deutschland import vag
from deutschland.vag.api import haltestellen_api
from deutschland.vag.model.haltestellen_api_response import HaltestellenAPIResponse
from pprint import pprint
# Defining the host is optional and defaults to https://start.vag.de/dm
# See configuration.py for a list of all supported configuration parameters.
configuration = vag.Configuration(
    host = "https://start.vag.de/dm"
)


# Enter a context with an instance of the API client
with vag.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = haltestellen_api.HaltestellenApi(api_client)
    netvu = "netvu_example" # str | Netz des Verkehrsunternehmen, aktuell \"VAG\" oder \"VGN\"
    name = "name_example" # str | Name der Haltestelle (like)

    # example passing only required values which don't have defaults set
    try:
        # Liefert die Liste mit den Haltestellen zu dem angegebenen Haltestellenname (Optional)
        api_response = api_instance.haltestellen_get_by_name(netvu, name)
        pprint(api_response)
    except vag.ApiException as e:
        print("Exception when calling HaltestellenApi->haltestellen_get_by_name: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **netvu** | **str**| Netz des Verkehrsunternehmen, aktuell \&quot;VAG\&quot; oder \&quot;VGN\&quot; |
 **name** | **str**| Name der Haltestelle (like) |

### Return type

[**HaltestellenAPIResponse**](HaltestellenAPIResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

