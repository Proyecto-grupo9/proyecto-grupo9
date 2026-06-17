def test_ventas_segment():
    assert ventas_segment("Standard Class","Consumer","United States","Fort Lauderdale","Florida","33311","South","Furniture","Tables","957.5775","5","0.45","-383.031,26.121561","-80.128778","") == -1
    assert ventas_segment("Standard Class","Consumer","United States","Fort Lauderdale","Florida","33311","South","Furniture","Tables","957.5775","5","0.45","-383.031,26.121561","-80.128778","Consumer") == 1)
    assert ventas_segment([], "Consumer") == -1