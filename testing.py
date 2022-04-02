import hourly_compensation_API as hc


def test_params_init():
    hc._init_params()

    assert 'WEEKDAY' in hc._hour_dict
    assert 'WEEKEND' in hc._hour_dict
    assert isinstance(hc._hour_dict['WEEKDAY'], dict)
    assert isinstance(hc._hour_dict['WEEKEND'], dict)


def test_get_day_type():
    hc._init_params()

    assert hc._get_day_type('MO') == 'WEEKDAY'
    assert hc._get_day_type('TU') == 'WEEKDAY'
    assert hc._get_day_type('WE') == 'WEEKDAY'
    assert hc._get_day_type('TH') == 'WEEKDAY'
    assert hc._get_day_type('FR') == 'WEEKDAY'
    assert hc._get_day_type('SA') == 'WEEKEND'
    assert hc._get_day_type('SU') == 'WEEKEND'


def test_get_hour_frame():
    hc._init_params()

    assert hc._get_hour_frame('00:01') == '00'
    assert hc._get_hour_frame('09:00') == '00'
    assert hc._get_hour_frame('09:01') == '09'
    assert hc._get_hour_frame('18:00') == '09'
    assert hc._get_hour_frame('18:01') == '18'
    assert hc._get_hour_frame('00:00') == '18'
    

def test_get_compensation():
    hc._init_params()
    
    assert hc._get_compensation('MO10:00-12:00') == 30
    assert hc._get_compensation('TU10:00-12:00') == 30
    assert hc._get_compensation('TH01:00-03:00') == 50
    assert hc._get_compensation('SA14:00-18:00') == 80
    assert hc._get_compensation('SU20:00-21:00') == 25


def test_process_worker_compensation():
    hc._init_params()

    assert hc.process_worker_compensation(
        'RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00'
    ) == 'The amount to pay RENE is: 215 USD'
    assert hc.process_worker_compensation(
        'ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00'
    ) == 'The amount to pay ASTRID is: 85 USD'

