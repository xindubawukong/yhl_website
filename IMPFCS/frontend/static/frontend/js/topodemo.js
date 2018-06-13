
function add_connection(source,destination){
var data=new Object();
data.source=source;
data.dest=destination;
arryAll.push(data);
}


function print_topo()
{

jsPlumb.ready(function () {

    // setup some defaults for jsPlumb.
    var instance = jsPlumb.getInstance({
        Endpoint: ["Dot", {radius: 2}],
        HoverPaintStyle: {strokeStyle: "#1e8151", lineWidth: 2 },
        ConnectionOverlays: [
           [ "Diamond", {
                location: 0.5,
                id: "diamond",
                length: 25
            } ]
			],

        Container: "statemachine-demo"
    });

    window.jsp = instance;
    var windows = jsPlumb.getSelector(".statemachine-demo .w");

    // initialise draggable elements.
    instance.draggable(windows);

    // bind a click listener to each connection; the connection is deleted. you could of course
    // just do this: jsPlumb.bind("click", jsPlumb.detach), but I wanted to make it clear what was
    // happening.
    instance.bind("click", function (c) {
    });

    // bind a connection listener. note that the parameter passed to this function contains more than
    // just the new connection - see the documentation for a full list of what is included in 'info'.
    // this listener sets the connection's internal
    // id as the label overlay's text.
    instance.bind("connection", function (info) {
        info.connection.getOverlay("label").setLabel(info.connection.id);
    });


    // suspend drawing and initialise.
    instance.batch(function () {
        instance.makeSource(windows, {
            filter: ".ep",
            anchor: "Continuous",
            connector: [ "StateMachine", { curviness: 20 } ],
            connectorStyle: { strokeStyle: "#5c96bc", lineWidth: 2, outlineColor: "transparent", outlineWidth: 4 },
            maxConnections: 5,
            onMaxConnections: function (info, e) {
                alert("Maximum connections (" + info.maxConnections + ") reached");
            }
        });

        // initialise all '.w' elements as connection targets.
        instance.makeTarget(windows, {
            dropOptions: { hoverClass: "dragHover" },
            anchor: "Continuous",
            allowLoopback: true
        });

        // and finally, make a couple of connections
		

		arryAll.forEach(function(data){  
        instance.connect({ source: data.source, target: data.dest });
			})
		//instance.connect({ source: "router2", target: "user3" });

    });

    jsPlumb.fire("jsPlumbDemoLoaded", instance);

});
}

setTimeout('print_topo()',1000);


