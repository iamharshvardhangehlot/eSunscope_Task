import dash
from dash import dcc, html, Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

# Load data from the database
engine = create_engine('mysql+pymysql://root:@localhost/esunscope')
employees_df = pd.read_sql('SELECT * FROM Employees', engine)

# Load each yearly work report and add a Year column
work_report_year1_df = pd.read_sql('SELECT * FROM WorkReports_Year1', engine)
work_report_year1_df['Year'] = 1
work_report_year2_df = pd.read_sql('SELECT * FROM WorkReports_Year2', engine)
work_report_year2_df['Year'] = 2
work_report_year3_df = pd.read_sql('SELECT * FROM WorkReports_Year3', engine)
work_report_year3_df['Year'] = 3
work_report_year4_df = pd.read_sql('SELECT * FROM WorkReports_Year4', engine)
work_report_year4_df['Year'] = 4

# Concatenate all yearly work reports
work_reports_df = pd.concat([work_report_year1_df, work_report_year2_df, work_report_year3_df, work_report_year4_df])

# Merge with employee details
merged_df = work_reports_df.merge(employees_df, on='EmployeeID', how='left')

# Initialize the Dash app with a Bootstrap theme
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.COSMO])

# Chart options for user selection
chart_options = {
    "Line Chart (Performance Over Time)": "line_chart",
    "Stacked Bar Chart (Projects by Department and Location)": "stacked_bar_chart",
    "Heatmap (Hours Worked vs. Performance Score)": "heatmap",
    "Bubble Chart (Feedback vs. Performance)": "bubble_chart",
    "Sunburst Chart (Department-Position Breakdown)": "sunburst_chart",
    "Histogram (Feedback Score Distribution)": "histogram",
    "Box Plot (Performance by Position)": "box_plot",
    "Radar Chart (Employee Progress)": "radar_chart"
}

# App layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("Employee Work Reports Dashboard", className="text-center text-primary my-4"), width=12)
    ]),

    # Filters row
    dbc.Row([
        dbc.Col([
            html.Label("Select Year(s)", style={'font-weight': 'bold'}),
            dcc.Dropdown(
                id='year-dropdown',
                options=[{'label': f'Year {i}', 'value': i} for i in range(1, 5)],
                value=[1],  # Default year
                clearable=False,
                multi=True,
                style={'border-radius': '5px', 'box-shadow': '0px 0px 4px #b0c4de'}
            )
        ], width=6, lg=3, className="mb-3"),
        
        dbc.Col([
            html.Label("Select Location(s)", style={'font-weight': 'bold'}),
            dcc.Dropdown(
                id='location-dropdown',
                options=[{'label': loc, 'value': loc} for loc in merged_df['Location'].unique()],
                value=['New York'],
                clearable=True,
                multi=True,
                style={'border-radius': '5px', 'box-shadow': '0px 0px 4px #b0c4de'}
            )
        ], width=6, lg=3, className="mb-3"),

        dbc.Col([
            html.Label("Select Department(s)", style={'font-weight': 'bold'}),
            dcc.Dropdown(
                id='department-dropdown',
                options=[{'label': dept, 'value': dept} for dept in merged_df['Department'].unique()],
                value=[],
                placeholder="Select Department(s)",
                clearable=True,
                multi=True,
                style={'border-radius': '5px', 'box-shadow': '0px 0px 4px #b0c4de'}
            )
        ], width=6, lg=3, className="mb-3"),

        dbc.Col([
            html.Label("Select Position(s)", style={'font-weight': 'bold'}),
            dcc.Dropdown(
                id='position-dropdown',
                options=[],  # Options will be populated based on selected department
                placeholder="Select Position(s)",
                clearable=True,
                multi=True,
                style={'border-radius': '5px', 'box-shadow': '0px 0px 4px #b0c4de'}
            )
        ], width=6, lg=3, className="mb-3"),
    ], justify="center", className="mb-4", style={'backgroundColor': '#f8f9fa', 'padding': '20px', 'border-radius': '10px'}),

    # Default charts row
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader("Projects Completed by Department", className="bg-primary text-white"),
                dbc.CardBody(
                    dcc.Graph(id='projects-completed-bar', config={'displayModeBar': False}),
                    style={'padding': '10px'}
                )
            ], style={'box-shadow': '0 4px 12px rgba(0, 0, 0, 0.1)', 'border-radius': '15px', 'margin': '10px'})
        ], width=12, lg=6, className="mb-4"),
        
        dbc.Col([
            dbc.Card([
                dbc.CardHeader("Department Distribution", className="bg-primary text-white"),
                dbc.CardBody(
                    dcc.Graph(id='department-distribution-pie', config={'displayModeBar': False}),
                    style={'padding': '10px'}
                )
            ], style={'box-shadow': '0 4px 12px rgba(0, 0, 0, 0.1)', 'border-radius': '15px', 'margin': '10px'})
        ], width=12, lg=6, className="mb-4")
    ]),

    # Chart selection and display for additional charts
    dbc.Row([
        dbc.Col([
            html.Label("Select Additional Chart to Display", style={'font-weight': 'bold'}),
            dcc.Dropdown(
                id='additional-chart-dropdown',
                options=[{'label': k, 'value': v} for k, v in chart_options.items()],
                placeholder="Select a chart",
                clearable=True
            ),
            dcc.Graph(id='additional-chart')
        ], width=12, lg=12, className="mb-4")
    ]),

    # Employee details table
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader("Employee Details", className="bg-primary text-white"),
                dbc.CardBody(
                    html.Div(id="employee-details")
                )
            ], style={'box-shadow': '0 4px 12px rgba(0, 0, 0, 0.1)', 'border-radius': '15px', 'margin': '10px'})
        ], width=12)
    ], className="mb-4")
], fluid=True)


@app.callback(
    Output('position-dropdown', 'options'),
    Input('department-dropdown', 'value')
)
def update_positions(selected_departments):
    if not selected_departments:
        return []
    filtered_positions = merged_df[merged_df['Department'].isin(selected_departments)][['Position', 'Department']].drop_duplicates()
    if len(selected_departments) > 1:
        options = [{'label': f"{row['Position']} ({row['Department']})", 'value': row['Position']} for _, row in filtered_positions.iterrows()]
    else:
        options = [{'label': position, 'value': position} for position in filtered_positions['Position'].unique()]
    return options


@app.callback(
    [Output('projects-completed-bar', 'figure'),
     Output('department-distribution-pie', 'figure'),
     Output('employee-details', 'children')],
    [Input('year-dropdown', 'value'),
     Input('location-dropdown', 'value'),
     Input('department-dropdown', 'value'),
     Input('position-dropdown', 'value')]
)
def update_charts(selected_year, selected_location, selected_department, selected_position):
    # Ensure inputs are lists to handle single/multiple selections
    if isinstance(selected_year, int):
        selected_year = [selected_year]
    if isinstance(selected_location, str):
        selected_location = [selected_location]
    if isinstance(selected_department, str):
        selected_department = [selected_department]
    if isinstance(selected_position, str):
        selected_position = [selected_position]

    # Start with filtering based on the selected year
    filtered_df = merged_df[merged_df['Year'].isin(selected_year)]

    # Apply location filter if specified
    if selected_location:
        filtered_df = filtered_df[filtered_df['Location'].isin(selected_location)]

    # Apply department filter if specified
    if selected_department:
        filtered_df = filtered_df[filtered_df['Department'].isin(selected_department)]

    # Apply position filter if specified
    if selected_position:
        filtered_df = filtered_df[filtered_df['Position'].isin(selected_position)]

    # Check if there’s data to display; otherwise, show a blank figure
    if filtered_df.empty:
        return {}, {}, html.P("No employee data available for the selected filters.", className="text-center")

    # Bar chart for Projects Completed
    bar_fig = px.bar(
        filtered_df,
        x='Department',
        y='ProjectsCompleted',
        color='Department',
        title='Projects Completed for Selected Years and Departments', 
        hover_data={'EmployeeID': True, 'Location': True, 'ProjectsCompleted': True}
    )
    bar_fig.update_layout(
        title={'x': 0.5, 'xanchor': 'center'},
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color="#333"),
        yaxis=dict(showgrid=False)
    )
    # Update hover template to show Employee ID, Location, and Projects Completed
    bar_fig.update_traces(
        hovertemplate='Employee ID: %{customdata[0]}<br>Location: %{customdata[1]}<br>Projects Completed: %{y}'
    )

    # Pie chart for Department Distribution
    pie_fig = px.pie(
        filtered_df,
        names='Department',
        title='Department Distribution for Selected Filters'
    )
    pie_fig.update_layout(
        title={'x': 0.5, 'xanchor': 'center'},
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color="#333")
    )
    pie_fig.update_traces(
        textinfo='percent+label',
        hovertemplate='%{label}: %{percent}'
    )

    # Employee details table
    employee_table = dbc.Table.from_dataframe(
        filtered_df[['EmployeeID', 'Name', 'Location', 'Department', 'Position', 'ProjectsCompleted', 'HoursWorked', 'PerformanceScore', 'FeedbackScore']],
        striped=True,
        bordered=True,
        hover=True,
        responsive=True,
        className="table-hover table-striped"
    )

    # Wrapping the table in a div with fixed height and overflow for scrolling
    employee_table_container = html.Div(
        employee_table,
        style={
            'maxHeight': '400px',  # Set max height to show around 10 entries
            'overflowY': 'auto'    # Enable vertical scrolling if entries exceed max height
        }
    )

    return bar_fig, pie_fig, employee_table_container


# Additional callback for displaying the selected additional chart
@app.callback(
    Output('additional-chart', 'figure'),
    [Input('additional-chart-dropdown', 'value'),
     Input('year-dropdown', 'value'),
     Input('location-dropdown', 'value'),
     Input('department-dropdown', 'value'),
     Input('position-dropdown', 'value')]
)
def update_additional_chart(chart_type, selected_year, selected_location, selected_department, selected_position):
    # Ensure inputs are lists to handle single/multiple selections
    if isinstance(selected_year, int):
        selected_year = [selected_year]
    if isinstance(selected_location, str):
        selected_location = [selected_location]
    if isinstance(selected_department, str):
        selected_department = [selected_department]
    if isinstance(selected_position, str):
        selected_position = [selected_position]

    # Start with filtering based on the selected year
    filtered_df = merged_df[merged_df['Year'].isin(selected_year)]

    # Apply location filter if specified
    if selected_location:
        filtered_df = filtered_df[filtered_df['Location'].isin(selected_location)]

    # Apply department filter if specified
    if selected_department:
        filtered_df = filtered_df[filtered_df['Department'].isin(selected_department)]

    # Apply position filter if specified
    if selected_position:
        filtered_df = filtered_df[filtered_df['Position'].isin(selected_position)]

    # Generate chart based on user-selected type
    if chart_type == "line_chart":
        fig = px.line(filtered_df, x='Month', y='PerformanceScore', color='Name', title="Employee Performance Over Time")
    elif chart_type == "stacked_bar_chart":
        fig = px.bar(filtered_df, x='Department', y='ProjectsCompleted', color='Location', barmode='stack', title="Projects by Department and Location")
    elif chart_type == "heatmap":
        fig = px.density_heatmap(filtered_df, x='HoursWorked', y='PerformanceScore', title="Hours Worked vs. Performance Score")
    elif chart_type == "bubble_chart":
        fig = px.scatter(filtered_df, x='FeedbackScore', y='PerformanceScore', size='ProjectsCompleted', color='Department', hover_name='Name', title="Feedback vs. Performance")
    elif chart_type == "sunburst_chart":
        fig = px.sunburst(filtered_df, path=['Department', 'Position', 'Name'], title="Department-Position Breakdown")
    elif chart_type == "histogram":
        fig = px.histogram(filtered_df, x='FeedbackScore', title="Feedback Score Distribution")
    elif chart_type == "box_plot":
        fig = px.box(filtered_df, x='Position', y='PerformanceScore', color='Position', title="Performance by Position")
    elif chart_type == "radar_chart":
        fig = px.line_polar(filtered_df, r='ProjectsCompleted', theta='Position', line_close=True, title="Employee Progress")
    else:
        fig = {}

    return fig


# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)

