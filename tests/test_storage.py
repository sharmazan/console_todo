from storage import save_tasks


def test_save_tasks(tmpdir):
    file = tmpdir.join("test.txt")
    tasks = ["hello", "world"]
    save_tasks(file.strpath, tasks)
    assert file.read() == "hello\nworld\n"
