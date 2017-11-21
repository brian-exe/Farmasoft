jQuery.fn.tableToCSV = function() {
    
	$(this).each(function(){
			var table = $(this);
			var caption = $(this).find('caption').text();
			var title = [];
			var rows = [];

			/*Recorro cada celda de la tabla y guardo el texto en una variable*/
			$(this).find('tr').each(function(){
				var data = [];
				$(this).find('th').each(function(){
					var text = $(this).text();
					title.push(text);
					});
				$(this).find('td').each(function(){
					var text = $(this).text();
					data.push(text);
					});
				data = data.join(",");
				rows.push(data);
				});
			title = title.join(",");
			rows = rows.join("\n");
			
			var csv = title + rows;
			var uri = 'data:text/csv;charset=utf-8,' + encodeURIComponent(csv);
			var download_link = document.createElement('a');
			download_link.id="link-descarga";
			download_link.href = uri;
			/*Genero el nombre*/
			var ts = new Date().getTime();
			var date = new Date();
			var fecha =date.toISOString().slice(0,10).replace(/-/g,"");
			var hora = date.toLocaleTimeString('es-AR').slice(0,8).trim().replace(/:/g,"")
			if(hora.length ==5){
				hora='0'+hora;
			}
			var nombreArchivo= 'resultados_'+fecha+'_'+hora;
			/*Fin*/
			download_link.download = nombreArchivo+".csv";
			
			document.body.appendChild(download_link);
			download_link.click();
			//document.body.removeChild(download_link);
	});
    
};
