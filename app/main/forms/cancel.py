from flask.ext.wtf import Form
from wtforms import RadioField, validators


class CancelBriefForm(Form):
    """Form for the buyer to tell us why they cancel the requirement
    """
    description_cancel = "The requirement has been cancelled"
    description_unsuccessful = "There were no suitable suppliers"
    reason = RadioField(
        "Reason for cancelling the requirement",
        validators=[validators.DataRequired(message="You need to answer this question.")],
        coerce=int,
        choices=[("cancel", description_cancel), ("unsuccessful", description_unsuccessful)]
    )
