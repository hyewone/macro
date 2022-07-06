
# 넷퍼넬 사용 대상 상품...
if (args[0] == "38096" || args[0] == "42082" || args[0] == "42074" || args[0] == "42123" || args[0] == "42169" || args[0] == "42231" || args[0] == "42232" || args[0] == "42353" || args[0] == "42357" || args[0] == "42449" || args[0] == "42451" || args[0] == "42452" || args[0] == "42453" || args[0] == "42595" || args[0] == "42630" || args[0] == "42534" || args[0] == "42711" || args[0] == "42746" || args[0] == "42769" || args[0] == "42784" || args[0] == "42802" || args[0] == "42732" || args[0] == "42673" || args[0] == "42534" || args[0] == "42747" || args[0] == "42701" || args[0] == "42804" || args[0] == "42805" || args[0] == "42806")
		{
			//Netfunnel 자원 사용 요청
		    //var dp = document.getElementById("debug_print");
		    var userid = $("#HidLoginID").val();

		    NetFunnel_Action({ action_id: "act_1", use_mobile_ui: "false", skin_id: "yesticket", user_data: userid }, {
				success:function(ev,ret){
				//실제 제어하고자 했던 Business Logic을 호출하시면 됩니다.
				/*
				var msg = "success:"
							+",code="+ret.code
							+",key="+ret.data.key
							+",ip="+ret.data.ip
							+",port="+ret.data.port
							+",nnext="+ret.data.nnext
							+",nwait="+ret.data.nwait
							+",tps="+ret.data.tps
							+",ttl="+ret.data.ttl;
				*/
				//dp.innerHTML += "<br>"+msg;
				//alert(msg);

				//alert(ret.data.key);


					var url = 'http://' + location.host + '/Pages/Perf/Sale/PerfSaleProcess.aspx' + paramString;
					var form = $("form");
					var target = 'pop_perfsale';
					window.open(url, target, "width=1000,height=700,resizable=yes,toolbar=yes,menubar=yes,location=yes");

					form.attr('action', url);
					form.attr('target', target); // window.open 타이틀과 매칭 되어야함
					form.attr('method', 'post');

					
					$("#netfunnel_key").remove();
					form.append('<input type="text" id="netfunnel_key" name="netfunnel_key" value="' + ret.data.key + '">'); // 동적으로 값을 추가할때  
					form.submit();
					$("#netfunnel_key").remove();

				},
				continued:function(ev,ret){
				//대기 상황에서 반복 호출되는 callback으로 필수는 아니며, 필요시 활성화해서 사용하시면 되겠습니다.

				},
				stop:function(ev,ret){
				//중지 버튼을 눌렀을 때 호출되는 callback으로 별도 처리하지 않을 경우, 대기창(div)가 hidden 및 destory 처리합니다.
				//중지 버튼을 눌렀을 때 별도 처리가 필요한 경우 사용하시면 되겠습니다.
					//alert("창 끄면 표 못 구한다!?");
					//alert(ret);

				},
				error:function(ev,ret){
				//넷퍼넬 장애로 인해 서비스에 영향을 미치면 안되기에, default로 error도 success와 동일하게 동작하도록 구성되어 있습니다.
				//따라서, error 상황일 때 별도 처리가 필요한 경우(특정 error page로 redirect 또는 별도 logging 처리 등)를 제외하고
				//error callback을 사용하지 않으시거나(미사용 시 success처리), success와 동일하게 구성하시길 권고드립니다.
					//alert('error netfunnel');
					//alert(ret.data.key);
					var jvPopupLeftPos = (screen.width - jvPopupWidth) / 2;
					var jvPopupTopPos = (screen.height - jvPopupHeight) / 2;

					var popUrl = 'http://' + location.host + '/Pages/Perf/Sale/PerfSaleProcess.aspx' + paramString + '&WaitErr=Y';
					
					if (!winRef || winRef.closed) {
							winRef = window.open(popUrl, 'pop_perfsale', 'width=' + jvPopupWidth + ',height=' + jvPopupHeight + ',left=' + jvPopupLeftPos + ',top=' + jvPopupTopPos);
					} else {
						winRef.location = popUrl;
						winRef.focus();
					}

				},
				bypass:function(ev,ret){
				//넷퍼넬 관리자페이지에서 해당 액션ID를 우회(bypass)처리했을 때 호출되는 callback으로 별도 처리가 필요한 경우 사용하실 수 있습니다.

				},
				block:function(ev,ret){
				//넷퍼넬 관리자페이지에서 해당 액션ID를 차단(block)처리했을 때 호출되는 callback으로 별도 처리가 필요한 경우 사용하실 수 있습니다.
				// ex) 10:00부터 서비스가 시작됩니다.   모든 상품이 소진되었습니다. 등에 활용

					NetFunnel.PopupSetup("alert", ret, "blockSkin");
					return false;
				},
				ipblock:function(ev,ret){
				//넷퍼넬 관리자페이지에서 액세스제어 기능을 활성화하고, 액세스제어 정책에 해당될 경우에만 호출되는 callback으로 
				//비정상적인 접근을 차단할 때 사용할 수 있습니다.

					NetFunnel.PopupSetup("alert", ret, "ipBlockSkin");
					return false;
				},
				expressnumber:function(ev,ret){
				//넷퍼넬 관리자페이지에서 액세스제어 기능을 활성화하고, express 항목에 등록된 IP/ID에 해당될 경우에만 호출되는 callback으로 
				//bypass 처리되며, 별도 처리가 필요할 경우 사용하실 수 있습니다.

				}
			});
		}
		else
		{
			var jvPopupLeftPos = (screen.width - jvPopupWidth) / 2;
			var jvPopupTopPos = (screen.height - jvPopupHeight) / 2;

			var popUrl = 'http://' + location.host + '/Pages/Perf/Sale/PerfSaleProcess.aspx' + paramString;
			
			if (!winRef || winRef.closed) {
					winRef = window.open(popUrl, 'pop_perfsale', 'width=' + jvPopupWidth + ',height=' + jvPopupHeight + ',left=' + jvPopupLeftPos + ',top=' + jvPopupTopPos);
			} else {
				winRef.location = popUrl;
				winRef.focus();
			}
		}