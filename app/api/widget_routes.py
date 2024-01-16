from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import User, Widget

widget_routes = Blueprint('widgets', __name__)

@widget_routes.route('', methods=['GET','POST'])
@login_required
def user_widgets():
    if request.method == 'GET':
        user_widgets = Widget.query.filter_by(user_id=current_user.id).all()

        widgets = [widget.to_widget_dict() for widget in user_widgets]

        return jsonify(widgets)
