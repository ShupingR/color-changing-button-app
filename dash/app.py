import dash
from dash import html, dcc, callback, Output, Input
import random

# Initialize the Dash app
app = dash.Dash(__name__)

# Define colors for the button
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7', '#DDA0DD', '#98D8C8', '#F7DC6F']

# Layout of the app
app.layout = html.Div([
    html.H1("Simple Color Changing Dashboard", 
            style={'textAlign': 'center', 'color': '#2c3e50', 'marginBottom': 30}),
    
    html.Div([
        html.Button(
            id='color-button',
            children='Click me to change color!',
            style={
                'fontSize': '18px',
                'padding': '15px 30px',
                'border': 'none',
                'borderRadius': '10px',
                'cursor': 'pointer',
                'backgroundColor': '#3498db',
                'color': 'white',
                'boxShadow': '0 4px 6px rgba(0, 0, 0, 0.1)',
                'transition': 'all 0.3s ease'
            }
        )
    ], style={'textAlign': 'center', 'marginBottom': 30}),
    
    html.Div([
        html.H3("Click count:", style={'textAlign': 'center', 'color': '#34495e'}),
        html.H2(id='click-count', style={'textAlign': 'center', 'color': '#e74c3c', 'fontSize': '48px'})
    ]),
    
    html.Div([
        html.P("This is a simple dashboard created with Dash and deployed on Render!", 
               style={'textAlign': 'center', 'color': '#7f8c8d', 'fontSize': '16px'})
    ], style={'marginTop': 50})
])

# Callback to update button color and click count
@callback(
    [Output('color-button', 'style'),
     Output('click-count', 'children')],
    [Input('color-button', 'n_clicks')],
    prevent_initial_call=True
)
def update_button_color(n_clicks):
    if n_clicks is None:
        return dash.no_update, dash.no_update
    
    # Get current style and update background color
    current_style = {
        'fontSize': '18px',
        'padding': '15px 30px',
        'border': 'none',
        'borderRadius': '10px',
        'cursor': 'pointer',
        'backgroundColor': random.choice(colors),
        'color': 'white',
        'boxShadow': '0 4px 6px rgba(0, 0, 0, 0.1)',
        'transition': 'all 0.3s ease'
    }
    
    return current_style, n_clicks

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=8050) 