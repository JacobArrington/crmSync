from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import User, Widget, Calculator, db

widget_routes = Blueprint('widgets', __name__)

@widget_routes.route('', methods=['GET'])
@login_required
def user_widgets():
    
    user_widgets = Widget.query.filter_by(user_id=current_user.id).all()

    widgets = [widget.to_widget_dict() for widget in user_widgets]

    return jsonify(widgets)


@widget_routes.route('', methods=['POST'])
@login_required
def widget_actions():
    data = request.json
    widget_type = data.get('widget_type')

    if widget_type == "Calculator":
        calculator_widget = Widget.query.filter_by(user_id=current_user.id, widget_type="Calculator").first()
        if not calculator_widget:
            calculator_widget = Widget(user_id=current_user.id, widget_type="Calculator")
            db.session.add(calculator_widget)
            db.session.commit()
#end of day
