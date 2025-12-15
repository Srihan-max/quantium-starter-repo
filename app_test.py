import pytest
import dash
from dash import dcc, html
from dash.testing.application_runners import import_app

def test_header_present(dash_duo):
    from app import app

    dash_duo.start_server(app)

    header = dash_duo.find_element("h1")
    assert header.text == "Pink Morsels Sales by Region"


def test_graph_present(dash_duo):
    from app import app

    dash_duo.start_server(app)

    graph = dash_duo.find_element("#sales-line-chart")
    assert graph is not None


def test_region_picker_present(dash_duo):
    from app import app

    dash_duo.start_server(app)

    radio = dash_duo.find_element("#region-radio")
    assert radio is not None
