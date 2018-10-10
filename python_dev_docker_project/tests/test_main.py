from python_dev_docker_project.__main__ import main


class TestMainFunc(object):
    def test_main_no_args(self, capsys):
        main(argv=[])

        out, err = capsys.readouterr()
        assert out == 'Hello!\n'
        assert err == ''

    def test_main_one_arg(self, capsys):
        main(argv=['World'])

        out, err = capsys.readouterr()
        assert out == 'Hello, World!\n'
        assert err == ''

    def test_main_multiple_args(self, capsys):
        main(argv=['Gino', 'Tesei'])

        out, err = capsys.readouterr()
        assert out == 'Hello, Gino Tesei!\n'
        assert err == ''
