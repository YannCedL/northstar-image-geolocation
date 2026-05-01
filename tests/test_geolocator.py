# test du moteur de géolocalisation solaire Northstar
from northstar_image_geolocation.geolocator import geolocate_image

def test_geolocate_image():
    contract = geolocate_image("photo.jpg")
    assert contract is not None
    assert contract.result["estimated_lat"] is not None
    assert contract.result["sun_azimuth_deg"] > 0
    assert len(contract.evidence) >= 1
