# vag.AbfahrtenApi

All URIs are relative to *https://start.vag.de/dm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**abfahrten_get1**](AbfahrtenApi.md#abfahrten_get1) | **GET** /api/v1/abfahrten/{netvu}/{haltid} | Liefert die Abfahrten zu einer bestimmten Haltestelle
[**abfahrten_get2**](AbfahrtenApi.md#abfahrten_get2) | **GET** /api/v1/abfahrten/{netvu}/{haltid}/{line} | Liefert die Abfahrten zu einer bestimmten Haltestelle


# **abfahrten_get1**
> AbfahrtenAPIResponse abfahrten_get1(netvu, haltid)

Liefert die Abfahrten zu einer bestimmten Haltestelle

### Example


```python
import time
from deutschland import vag
from deutschland.vag.api import abfahrten_api
from deutschland.vag.model.abfahrten_api_response import AbfahrtenAPIResponse
from pprint import pprint
# Defining the host is optional and defaults to https://start.vag.de/dm
# See configuration.py for a list of all supported configuration parameters.
configuration = vag.Configuration(
    host = "https://start.vag.de/dm"
)


# Enter a context with an instance of the API client
with vag.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = abfahrten_api.AbfahrtenApi(api_client)
    netvu = "netvu_example" # str | Netz des Verkehrsunternehmen, aktuell \"VAG\" oder \"VGN\"
    haltid = "haltid_example" # str | Haltestellenkennung je nach NetVU - VGN-Kennung oder die HaltID der VAG
    product = "product_example" # str | Betriebszweig der VAG Bus, Tram, UBahn. Querystring: product=Bus,Tram (optional)
    timespan = 1 # int | Zeitfenster für die Abfrage in Minuten (?timespan=10) (optional)
    timedelay = 1 # int | Zeitliche Verschiebung für die Anfrage in Minuten (?timedelay=5) (optional)
    limitcount = 1 # int | Maximale Anzahl der zurückgelieferten Abfahrten (optional)

    # example passing only required values which don't have defaults set
    try:
        # Liefert die Abfahrten zu einer bestimmten Haltestelle
        api_response = api_instance.abfahrten_get1(netvu, haltid)
        pprint(api_response)
    except vag.ApiException as e:
        print("Exception when calling AbfahrtenApi->abfahrten_get1: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Liefert die Abfahrten zu einer bestimmten Haltestelle
        api_response = api_instance.abfahrten_get1(netvu, haltid, product=product, timespan=timespan, timedelay=timedelay, limitcount=limitcount)
        pprint(api_response)
    except vag.ApiException as e:
        print("Exception when calling AbfahrtenApi->abfahrten_get1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **netvu** | **str**| Netz des Verkehrsunternehmen, aktuell \&quot;VAG\&quot; oder \&quot;VGN\&quot; |
 **haltid** | **str**| Haltestellenkennung je nach NetVU - VGN-Kennung oder die HaltID der VAG |
 **product** | **str**| Betriebszweig der VAG Bus, Tram, UBahn. Querystring: product&#x3D;Bus,Tram | [optional]
 **timespan** | **int**| Zeitfenster für die Abfrage in Minuten (?timespan&#x3D;10) | [optional]
 **timedelay** | **int**| Zeitliche Verschiebung für die Anfrage in Minuten (?timedelay&#x3D;5) | [optional]
 **limitcount** | **int**| Maximale Anzahl der zurückgelieferten Abfahrten | [optional]

### Return type

[**AbfahrtenAPIResponse**](AbfahrtenAPIResponse.md)

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

# **abfahrten_get2**
> AbfahrtenAPIResponse abfahrten_get2(netvu, haltid, line)

Liefert die Abfahrten zu einer bestimmten Haltestelle

### Example


```python
import time
from deutschland import vag
from deutschland.vag.api import abfahrten_api
from deutschland.vag.model.abfahrten_api_response import AbfahrtenAPIResponse
from pprint import pprint
# Defining the host is optional and defaults to https://start.vag.de/dm
# See configuration.py for a list of all supported configuration parameters.
configuration = vag.Configuration(
    host = "https://start.vag.de/dm"
)


# Enter a context with an instance of the API client
with vag.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = abfahrten_api.AbfahrtenApi(api_client)
    netvu = "netvu_example" # str | Netz des Verkehrsunternehmen, aktuell \"VAG\" oder \"VGN\"
    haltid = "haltid_example" # str | Haltestellenkennung je nach NetVU - VGN-Kennung oder die HaltID der VAG
    line = "line_example" # str | Linienkürzel der VAG
    product = "product_example" # str | Betriebszweig der VAG Bus, Tram, UBahn. Querystring: product=Bus,Tram (optional)
    timespan = 1 # int | Zeitfenster für die Abfrage in Minuten (?timespan=10) (optional)
    timedelay = 1 # int | Zeitliche Verschiebung für die Anfrage in Minuten (?timedelay=5) (optional)
    limitcount = 1 # int | Maximale Anzahl der zurückgelieferten Abfahrten (optional)

    # example passing only required values which don't have defaults set
    try:
        # Liefert die Abfahrten zu einer bestimmten Haltestelle
        api_response = api_instance.abfahrten_get2(netvu, haltid, line)
        pprint(api_response)
    except vag.ApiException as e:
        print("Exception when calling AbfahrtenApi->abfahrten_get2: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Liefert die Abfahrten zu einer bestimmten Haltestelle
        api_response = api_instance.abfahrten_get2(netvu, haltid, line, product=product, timespan=timespan, timedelay=timedelay, limitcount=limitcount)
        pprint(api_response)
    except vag.ApiException as e:
        print("Exception when calling AbfahrtenApi->abfahrten_get2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **netvu** | **str**| Netz des Verkehrsunternehmen, aktuell \&quot;VAG\&quot; oder \&quot;VGN\&quot; |
 **haltid** | **str**| Haltestellenkennung je nach NetVU - VGN-Kennung oder die HaltID der VAG |
 **line** | **str**| Linienkürzel der VAG |
 **product** | **str**| Betriebszweig der VAG Bus, Tram, UBahn. Querystring: product&#x3D;Bus,Tram | [optional]
 **timespan** | **int**| Zeitfenster für die Abfrage in Minuten (?timespan&#x3D;10) | [optional]
 **timedelay** | **int**| Zeitliche Verschiebung für die Anfrage in Minuten (?timedelay&#x3D;5) | [optional]
 **limitcount** | **int**| Maximale Anzahl der zurückgelieferten Abfahrten | [optional]

### Return type

[**AbfahrtenAPIResponse**](AbfahrtenAPIResponse.md)

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

