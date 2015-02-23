from . import main
from app import models
from flask import abort, render_template, request, jsonify, Response
from ..helpers.presenters import SearchResults

def get_template_data(blueprint, view_data):
    template_data = blueprint.config['BASE_TEMPLATE_DATA']
    for key in view_data:
        template_data[key] = view_data[key];
    return template_data

@main.route('/')
def index():
    return "Hello, World!", 200

@main.route('/service/<service_id>')
def get_service_by_id(service_id):
    try:
        service = models.get_service(service_id)
        return Response(service, mimetype='application/json')
    except KeyError:
        abort(404, "Service ID '%s' can not be found" % service_id)


@main.route('/search/<query>')
def search(query):
    response = models.search_for_service(query)
    search_results_obj = SearchResults(response)
    template_data = get_template_data(main, {
        'title' : 'Search results',
        'services' : search_results_obj.get_results()['services']
    })
    return render_template('search.html', **template_data)

@main.route('/search/<query>/<lot>')
def search_with_lot(query, lot):
    response = models.search_with_lot_filter(query, lot)
    search_results_obj = SearchResults(response)
    template_data = get_template_data(main, {
        'title' : 'Search results',
        'services' : search_results_obj.get_results()['services']
    })
    return render_template('search.html', **template_data)

@main.route('/search/<query>/filter')
def search_with_filters(query):
    response = models.search_with_filters(query, request.args)
    search_results_obj = SearchResults(response)
    template_data = get_template_data(main, {
        'title' : 'Search results',
        'services' : search_results_obj.get_results()['services']
    })
    return render_template('search.html', **template_data)

@main.route('/test')
def test():
    template_data = main.config['BASE_TEMPLATE_DATA']
    template_data['title'] = 'test page'
    return render_template('test.html', **template_data)

