import asyncio
from weather import get_forecast, get_alerts

async def test_weather():
    # Test San Francisco forecast (coordinates)
    print("=== San Francisco Forecast ===")
    forecast = await get_forecast(37.7749, -122.4194)
    print(forecast)
    
    print("\n=== California Alerts ===")
    alerts = await get_alerts("CA")
    print(alerts)

if __name__ == "__main__":
    asyncio.run(test_weather())