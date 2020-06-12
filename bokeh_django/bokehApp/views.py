from django.shortcuts import render
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.models import HoverTool,LassoSelectTool,WheelZoomTool,PointDrawTool,ColumnDataSource
from bokeh.palettes import Category20c,Spectral6
from .models import Products

# Create your views here.
def home(request):

    plot = figure()
    plot.circle([1,10,35,157],[0,0,0,0],size=20,color="blue")

    script ,div = components(plot) # returns indivual element
    template = 'home.html'
    context = {'script':script,'div':div}

    return render(request,template,context)
    
def secondGraph(request):

    template = 'second.html'

    x = [1,2,3,4,5]
    y = [6,10,2,-4,10]
    title = 'Leaning Graph'

    plot = figure(title=title,
        x_axis_label = 'High and Low',
        y_axis_label = 'Learning Topics',

        plot_width  = 700,
        plot_height = 700,
        tools       = "",
        toolbar_location = None,
    )

    #Fromating Graph
    cr = plot.circle(x,y,size=10,color="blue",fill_color="grey",hover_fill_color="firebrick",
                    fill_alpha=0.05, hover_alpha=0.3,
                    line_color=None,hover_line_color="white")


    plot.add_tools(HoverTool(tooltips=None,renderers=[cr],mode='hline'))
    plot.title.text_font_size = '20pt'
    plot.line(x,y,legend_label='Leaning Line',line_width=4,line_color="brown",line_dash="dashed")
    plot.background_fill_color = "lightgrey"
    plot.border_fill_color = "whitesmoke"
    plot.min_border_left = 40
    plot.min_border_right = 40
    plot.outline_line_width = 7
    plot.outline_line_alpha = 0.2
    plot.outline_line_color = "purple"

    #store components
    script , div = components(plot)

    context  = {'script':script,'div':div}
    
    return render(request,template,context)

def product_page(request):
    template = 'products.html'
    
    car_price = []
    car_model = []

    cars = []
    price = []

    
    car_price = Products.objects.values_list('price',flat=True)
    car_model = Products.objects.values_list('name',flat=True)

    

    for prc in car_price:
        price.append(prc)

    for model in car_model:
        cars.append(model)


    print(price)
    print(cars)
    
    p = figure(x_range=cars,plot_height=450,title='Car Price in Dollar',toolbar_location="below",
                tools="pan,wheel_zoom,box_zoom,reset,hover,tap,crosshair"
    )

    source = ColumnDataSource(data=dict(cars=cars,price=price,color=Spectral6))
    p.add_tools(LassoSelectTool())
    p.add_tools(WheelZoomTool())

    p.vbar(x='cars',top='price',width=.8,color='color',legend='cars',source=source)
    p.legend.orientation = "horizontal"
    p.legend.location  = "top_center"

    p.xgrid.grid_line_color = "black"
    p.y_range.start = 0
    p.line(x=cars,y=price,color="black",line_width=2)

    script,div = components(p)

    print(script)
    print(div)
    context = {'script':script,'div':div}

    return render(request,template,context)



def programming(request):
    
    lang = ['Python', 'JavaScript', 'C#', 'PHP', 'C++', 'Java']
    counts = [25, 30, 8, 22, 12, 17]

    p = figure(x_range=lang, plot_height=450, title="Programming Languages Popularity",
           toolbar_location="below", tools="pan,wheel_zoom,box_zoom,reset, hover, tap, crosshair")
    
    source = ColumnDataSource(data=dict(lang=lang, counts=counts, color=Spectral6))
    p.add_tools(LassoSelectTool())
    p.add_tools(WheelZoomTool())       

    p.vbar(x='lang', top='counts', width=.8, color='color', legend="lang", source=source)
    p.legend.orientation = "horizontal"
    p.legend.location = "top_center"

    p.xgrid.grid_line_color = "black"
    p.y_range.start = 0
    p.line(x=lang, y=counts, color="black", line_width=2)

    script, div = components(p)

    return render(request, 'programming.html' , {'script': script, 'div':div})