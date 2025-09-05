from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from models import db, Channel
from decorators import admin_required

channels_bp = Blueprint("channels", __name__)

@channels_bp.route("/admin")
@login_required
@admin_required
def dashboard():
    channels = Channel.query.order_by(Channel.created_at.desc()).all()
    return render_template("admin_dashboard.html", channels=channels)

@channels_bp.route("/admin/channels/new", methods=["GET", "POST"])
@login_required
@admin_required
def new_channel():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        url = request.form.get("url", "").strip()
        category = request.form.get("category", "").strip() or None
        is_public = bool(request.form.get("is_public"))
        if not name or not url:
            flash("İsim ve URL zorunludur.", "danger")
        else:
            ch = Channel(name=name, url=url, category=category, is_public=is_public)
            db.session.add(ch)
            db.session.commit()
            flash("Kanal eklendi.", "success")
            return redirect(url_for("channels.dashboard"))
    return render_template("admin_channel_form.html", channel=None)

@channels_bp.route("/admin/channels/<int:channel_id>/edit", methods=["GET", "POST"])
@login_required
@admin_required
def edit_channel(channel_id):
    ch = Channel.query.get_or_404(channel_id)
    if request.method == "POST":
        ch.name = request.form.get("name", "").strip()
        ch.url = request.form.get("url", "").strip()
        ch.category = request.form.get("category", "").strip() or None
        ch.is_public = bool(request.form.get("is_public"))
        if not ch.name or not ch.url:
            flash("İsim ve URL zorunludur.", "danger")
        else:
            db.session.commit()
            flash("Kanal güncellendi.", "success")
            return redirect(url_for("channels.dashboard"))
    return render_template("admin_channel_form.html", channel=ch)

@channels_bp.route("/admin/channels/<int:channel_id>/delete", methods=["POST"])
@login_required
@admin_required
def delete_channel(channel_id):
    ch = Channel.query.get_or_404(channel_id)
    db.session.delete(ch)
    db.session.commit()
    flash("Kanal silindi.", "success")
    return redirect(url_for("channels.dashboard"))
