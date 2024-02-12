class TestClassDemoInstance:
    value=0
    def test_one(self):
        self.value=1
        assert self.value==1
    def test_tow(self):
        assert self.value==1
