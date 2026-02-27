{
    "name": "Voice Note in Chatter",
    "version": "17.0.1.0.0",
    "summary": "Record voice note from chatter",
    "depends": ["mail"],
    "assets": {
        "web.assets_backend": [
            "chatter_voice_note/static/src/js/voice_recorder.js",
            "chatter_voice_note/static/src/xml/voice_button.xml",
        ],
    },
    "data": [
        # "views/voice_note_template.xml",
    ],
    "installable": True,
}