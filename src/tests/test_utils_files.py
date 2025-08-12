import os.path

from wpilib_cli.utils import files


def test_reverse_domain_with_valid_domain():
    assert files.reverse_domain("mckinleyfirebirds.com", "1915") == "com.mckinleyfirebirds"
    assert files.reverse_domain("itshao.me", "1915") == "me.itshao"
    assert files.reverse_domain("omg.AdrianJohnson.mit.edu", "1915") == "edu.mit.adrianjohnson.omg"


def test_reverse_domain_with_none():
    assert files.reverse_domain(None, "1915") == "org.team1915.frc"


def test_reverse_domain_with_empty_string():
    assert files.reverse_domain("", "1915") == "org.team1915.frc"
    assert files.reverse_domain("   ", "1915") == "org.team1915.frc"


def test_convert_domain_to_path_with_valid_domain():
    expected = os.path.join("com", "mckinleyfirebirds")
    assert files.convert_domain_to_path("mckinleyfirebirds.com", "1915") == expected
