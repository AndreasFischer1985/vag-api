# vag.FahrtenApi

All URIs are relative to *https://start.vag.de/dm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fahrten_get**](FahrtenApi.md#fahrten_get) | **GET** /api/v1/fahrten/{betriebszweig} | Liefert alle laufenden und startenden Fahrten zu dem angegebenen Betriebszweig innerhalb des angegebenen Zeitfenster.
[**fahrten_get_fahrt1**](FahrtenApi.md#fahrten_get_fahrt1) | **GET** /api/v1/fahrten/{betriebszweig}/{fahrtnummer} | Liefert die Fahrt des angegebenen Betriebszweig mit der Fahrtnummer und dem aktuellen Betriebstag
[**fahrten_get_fahrt2**](FahrtenApi.md#fahrten_get_fahrt2) | **GET** /api/v1/fahrten/{betriebszweig}/{betriebstag}/{fahrtnummer} | Liefert die Fahrt des angegebenen Betriebszweig mit der Fahrtnummer und dem angegebenen Betriebstag


# **fahrten_get**
> FahrtenAPIResponse fahrten_get(betriebszweig)

Liefert alle laufenden und startenden Fahrten zu dem angegebenen Betriebszweig innerhalb des angegebenen Zeitfenster.

### Example


```python
import time
from deutschland import vag
from deutschland.vag.api import fahrten_api
from deutschland.vag.model.fahrten_api_response import FahrtenAPIResponse
from pprint import pprint
# Defining the host is optional and defaults to https://start.vag.de/dm
# See configuration.py for a list of all supported configuration parameters.
configuration = vag.Configuration(
    host = "https://start.vag.de/dm"
)


# Enter a context with an instance of the API client
with vag.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = fahrten_api.FahrtenApi(api_client)
    betriebszweig = "betriebszweig_example" # str | Betriebszweig der VAG: Bus|Tram|UBahn
    timespan = 1 # int | Zeitfenster für die Abfrage in Minuten (Default 60 Minuten) (optional)

    # example passing only required values which don't have defaults set
    try:
        # Liefert alle laufenden und startenden Fahrten zu dem angegebenen Betriebszweig innerhalb des angegebenen Zeitfenster.
        api_response = api_instance.fahrten_get(betriebszweig)
        pprint(api_response)
    except vag.ApiException as e:
        print("Exception when calling FahrtenApi->fahrten_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Liefert alle laufenden und startenden Fahrten zu dem angegebenen Betriebszweig innerhalb des angegebenen Zeitfenster.
        api_response = api_instance.fahrten_get(betriebszweig, timespan=timespan)
        pprint(api_response)
    except vag.ApiException as e:
        print("Exception when calling FahrtenApi->fahrten_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **betriebszweig** | **str**| Betriebszweig der VAG: Bus|Tram|UBahn |
 **timespan** | **int**| Zeitfenster für die Abfrage in Minuten (Default 60 Minuten) | [optional]

### Return type

[**FahrtenAPIResponse**](FahrtenAPIResponse.md)

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

# **fahrten_get_fahrt1**
> FahrtenAPIResponse fahrten_get_fahrt1(betriebszweig, fahrtnummer)

Liefert die Fahrt des angegebenen Betriebszweig mit der Fahrtnummer und dem aktuellen Betriebstag

### Example


```python
import time
from deutschland import vag
from deutschland.vag.api import fahrten_api
from deutschland.vag.model.fahrten_api_response import FahrtenAPIResponse
from pprint import pprint
# Defining the host is optional and defaults to https://start.vag.de/dm
# See configuration.py for a list of all supported configuration parameters.
configuration = vag.Configuration(
    host = "https://start.vag.de/dm"
)


# Enter a context with an instance of the API client
with vag.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = fahrten_api.FahrtenApi(api_client)
    betriebszweig = "betriebszweig_example" # str | Betriebszweig der VAG: Bus|Tram|UBahn
    fahrtnummer = 1 # int | Fahrtnummer für die Anfrage

    # example passing only required values which don't have defaults set
    try:
        # Liefert die Fahrt des angegebenen Betriebszweig mit der Fahrtnummer und dem aktuellen Betriebstag
        api_response = api_instance.fahrten_get_fahrt1(betriebszweig, fahrtnummer)
        pprint(api_response)
    except vag.ApiException as e:
        print("Exception when calling FahrtenApi->fahrten_get_fahrt1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **betriebszweig** | **str**| Betriebszweig der VAG: Bus|Tram|UBahn |
 **fahrtnummer** | **int**| Fahrtnummer für die Anfrage |

### Return type

[**FahrtenAPIResponse**](FahrtenAPIResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | NotFound |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fahrten_get_fahrt2**
> FahrtenAPIResponse fahrten_get_fahrt2(betriebszweig, betriebstag, fahrtnummer)

Liefert die Fahrt des angegebenen Betriebszweig mit der Fahrtnummer und dem angegebenen Betriebstag

### Example


```python
import time
from deutschland import vag
from deutschland.vag.api import fahrten_api
from deutschland.vag.model.fahrten_api_response import FahrtenAPIResponse
from pprint import pprint
# Defining the host is optional and defaults to https://start.vag.de/dm
# See configuration.py for a list of all supported configuration parameters.
configuration = vag.Configuration(
    host = "https://start.vag.de/dm"
)


# Enter a context with an instance of the API client
with vag.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = fahrten_api.FahrtenApi(api_client)
    betriebszweig = "betriebszweig_example" # str | Betriebszweig der VAG: Bus|Tram|UBahn
    betriebstag = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Betriebstagsdatum für die Anfrag
    fahrtnummer = 1 # int | Fahrtnummer für die Anfrage

    # example passing only required values which don't have defaults set
    try:
        # Liefert die Fahrt des angegebenen Betriebszweig mit der Fahrtnummer und dem angegebenen Betriebstag
        api_response = api_instance.fahrten_get_fahrt2(betriebszweig, betriebstag, fahrtnummer)
        pprint(api_response)
    except vag.ApiException as e:
        print("Exception when calling FahrtenApi->fahrten_get_fahrt2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **betriebszweig** | **str**| Betriebszweig der VAG: Bus|Tram|UBahn |
 **betriebstag** | **datetime**| Betriebstagsdatum für die Anfrag |
 **fahrtnummer** | **int**| Fahrtnummer für die Anfrage |

### Return type

[**FahrtenAPIResponse**](FahrtenAPIResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | NotFound |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

