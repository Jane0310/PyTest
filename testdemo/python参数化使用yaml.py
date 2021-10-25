import pytest
import yaml
class TestYaml:

    @pytest.mark.parametrize(["a","b"],yaml.safe_load(open("yamlparam.yml")))
    def test_param(self,a,b):
        print(a+b)

if __name__ == '__main__':
    pytest.main()