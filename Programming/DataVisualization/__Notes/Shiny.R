# shiny/ 02_howToStart

# all of these are different examples of how to make your shiny app look nicer. 
# they all share the same server code, all that differs is the function for visualization

#######################################

library(shiny)

ui <- fluidPage( # makes a responsive page
  fluidRow(
   column(3, "Something"),
   column(5, sliderInput(inputId = "num", 
     label = "Choose a number", 
     value = 25, min = 1, max = 100))
  ),
  fluidRow(
    column(4, offset = 8,
      plotOutput("hist")
    )
  )
)

server <- function(input, output) {
  output$hist <- renderPlot({
    hist(rnorm(input$num))
  })
}

shinyApp(ui = ui, server = server)

######################################### tabs

ui <- fluidPage(title = "Random generator",
  tabsetPanel(     # makes 3 different tabs, each do different things
    # first tab takes norm, defined in server, which returns
    tabPanel(title = "Normal data",
      plotOutput("norm"),
      actionButton("renorm", "Resample")
    ),

    tabPanel(title = "Uniform data",
      plotOutput("unif"),
      actionButton("reunif", "Resample")
    ),

    tabPanel(title = "Chi Squared data",
      plotOutput("chisq"),
      actionButton("rechisq", "Resample")
    )
  )
)

######################################### navigation lists

ui <- fluidPage(title = "Random generator",
  navlistPanel(      # makes a navigation list with 3 panels, all do the same thing as above
                     # essentially vertical tabs        
    tabPanel(title = "Normal data",
      plotOutput("norm"),
      actionButton("renorm", "Resample")
    ),
    tabPanel(title = "Uniform data",
      plotOutput("unif"),
      actionButton("reunif", "Resample")
    ),
    tabPanel(title = "Chi Squared data",
      plotOutput("chisq"),
      actionButton("rechisq", "Resample")
    )
  )
)

############################################# sidebar

ui <- fluidPage(
  sidebarLayout(
    sidebarPanel(
      sliderInput(inputId = "num", 
        label = "Choose a number", 
        value = 25, min = 1, max = 100),
      textInput(inputId = "title", 
        label = "Write a title",
        value = "Histogram of Random Normal Values")
    ),
    mainPanel(
      plotOutput("hist")
    )
  )
)

############################################ navbar page

ui <- navbarPage(title = "Random generator",
  # instead of fluidpage, makes a navbarpage, which are fluid as well..
    tabPanel(title = "Normal data",
      plotOutput("norm"),
      actionButton("renorm", "Resample")
    ),
    tabPanel(title = "Uniform data",
      plotOutput("unif"),
      actionButton("reunif", "Resample")
    ),
    tabPanel(title = "Chi Squared data",
      plotOutput("chisq"),
      actionButton("rechisq", "Resample")
    )

)

############################################ navbar menu page

# includes a pull down option

ui <- navbarPage(title = "Random generator",
  tabPanel(title = "Normal data",
    plotOutput("norm"),
    actionButton("renorm", "Resample")
  ),
  navbarMenu(title = "Other data",
    tabPanel(title = "Uniform data",
      plotOutput("unif"),
      actionButton("reunif", "Resample")
    ),
    tabPanel(title = "Chi Squared data",
      plotOutput("chisq"),
      actionButton("rechisq", "Resample")
    )
  )
)

# to check if server is the same for all these code, go to command line and use the 'diff' function


###################################### server

# server.R
require("jsonlite")
require("RCurl")
require(ggplot2)
require(dplyr)
require(shiny)

shinyServer(function(input, output) {

  output$distPlot <- renderPlot({

  # output = sends from server to client



  # Start your code here.

  # The following is equivalent to KPI Story 2 Sheet 2 and Parameters Story 3 in "Crosstabs, KPIs, Barchart.twb"
      
  KPI_Low_Max_value = input$KPI1     
  # taking things from UI (slider), takes the value, and gets stored in this variable
  KPI_Medium_Max_value = input$KPI2
  # same as above. You will find the KPI2 function in the UI tab under 05 or something


  # this big chunk pulls data from an oracle database     
  df <- data.frame(fromJSON(getURL(URLencode(gsub("\n", " ", 

  # this big chunk is the SQL code it's sending to the server
  # if we use dplyr, the server returns all the data to my machine
  # This SQL is good for limiting all of it before it gets to my machine

  # The case part converts KPI from a huge number (measure) to a dimension
  # P1 and P2 are set at the bottom of the chunk
  # the reason P1 is surrounded in quotes is to exclude it from the SQL, 
  #   where it is assigned at the bottom
  # NOTE!!! Where P1 is, you can put ANY python expression, because his server is a python interpreter
  'oraclerest.cs.utexas.edu:5001/rest/native/?query=
  "select color, clarity, sum_price, round(sum_carat) as sum_carat, kpi as ratio, 
  case
  when kpi < "p1" then \\\'03 Low\\\'
  when kpi < "p2" then \\\'02 Medium\\\'
  else \\\'01 High\\\'
  end kpi
  from 
    ( 
  select color, clarity, 
  sum(price) as sum_price, sum(carat) as sum_carat, 
  sum(price) / sum(carat) as kpi
  from diamonds
  group by color, clarity
    )
  order by clarity;"
  ')), 
  # end SQL
  httpheader=c(DB='jdbc:oracle:thin:@aevum.cs.utexas.edu:1521/f16pdb', USER='cs329e_UTEid', PASS='orcl_uteid', MODE='native_mode', MODEL='model', returnDimensions = 'False', returnFor = 'JSON', p1=KPI_Low_Max_value, p2=KPI_Medium_Max_value), verbose = TRUE)))
  
  # The line below does all of this using dplyr

# df <- diamonds %>% group_by(color, clarity) %>% summarize(sum_price = sum(price), sum_carat = sum(carat)) %>% mutate(ratio = sum_price / sum_carat) %>% mutate(kpi = ifelse(ratio <= KPI_Low_Max_value, '03 Low', ifelse(ratio <= KPI_Medium_Max_value, '02 Medium', '01 High'))) %>% rename(COLOR=color, CLARITY=clarity, SUM_PRICE=sum_price, SUM_CARAT=sum_carat, RATIO=ratio, KPI=kpi)
      
  plot <- ggplot() + 
        coord_cartesian() + 
        scale_x_discrete() +
        scale_y_discrete() +
        labs(title='Diamonds Crosstab\nSUM_PRICE, SUM_CARAT, SUM_PRICE / SUM_CARAT') +
        labs(x=paste("COLOR"), y=paste("CLARITY")) +
        layer(data=df, 
              mapping=aes(x=COLOR, y=CLARITY, label=SUM_PRICE), 
              stat="identity", 
              #stat_params=list(), 
              geom="text",
              geom_params=list(color="black"), 
              position=position_identity()
        ) +
        layer(data=df, 
              mapping=aes(x=COLOR, y=CLARITY, fill=KPI), 
              stat="identity", 
              #stat_params=list(), 
              geom="tile",
              geom_params=list(alpha=0.50), 
              position=position_identity()
        )

  # End your code here.
        return(plot)
  }) # output$distPlot
})