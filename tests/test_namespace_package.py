def test_namespace_package() -> None:
    from numeus.package.file import foo

    assert foo() == 'bar'
