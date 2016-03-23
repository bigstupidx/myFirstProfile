function setLocalData(t,a){try{return window.localStorage.setItem(t,JSON.stringify(a)),!0}catch(e){return console.log("Storage数据失败! ["+e.toString()+"]"),!1}}function getLocalData(t){try{if(t in window.localStorage)return $.parseJSON(window.localStorage.getItem(t))}catch(a){return!1}}function delLocalData(t,a){try{t in window.localStorage?(window.localStorage.removeItem(t),"function"==typeof a&&a()):t in localStorage?(localStorage.removeItem(t),"function"==typeof a&&a()):(localStorage.removeItem(t),"function"==typeof a&&a())}catch(e){}}function getTaskState(){$.ajax({url:"/task/task_status/",type:"get",datatype:"json",success:function(t){"ok"==t.status&&"reward_to_receive"==t.msg&&$("#js-task-state").removeClass("task-state-undo").addClass("task-state-finish"),"ok"==t.status&&"task_to_do"==t.msg&&$("#js-task-state").removeClass("task-state-finish").addClass("task-state-undo"),"ok"==t.status&&"all_finished"==t.msg&&$("#js-task-state").removeClass("task-state-finish").addClass("task-state-all-finish")}})}function showLoading(t,a){a?$(t).find("span.data-loading").remove():$(t).append('<span class="data-loading"></span>')}function getTaskData(){var t=5,a=!1;$(".black-bg,#js-task-content").show(),showLoading("#js-task-content",a),$.ajax({url:"/task/",type:"get",datatype:"json",success:function(a){"ok"==a.status&&(fillSpeaker(a),growTaskHtml(1,5,a),$(".js-task-page").createPage({pageCount:Math.ceil(a.task_count/t),current:1,backFn:function(t){var e=!1;showLoading("#js-all-task",e),growTaskHtml(t,5,a)}}))}})}function fillSpeaker(t){for(var a="",e=t.recent,s=0;s<e.length;s++)a+="<li>"+e[s]+"</li>";$(".js-speaker").empty().append(a)}function AutoScroll(t,a){$(t).find("li").length>1&&$(t).find("ul:first").animate({marginTop:a},500,function(){$(this).css({marginTop:"0px"}).find("li:first").appendTo(this)})}function growTaskHtml(t,a,e){var s='<li><div class="task-name-title float-left task-name-title-public align-left">任务名称</div><div class="task-number-title float-left task-name-title-public">完成度</div><div class="task-gift-title float-left task-name-title-public">奖励</div></li>',n=e,i=(getLocalData("rewardData"),0);i=a*t<=n.data.length?a*t:n.data.length;for(var r=a*(t-1);i>r;r++){var o="";1==n.data[r].task_type&&(o+="【新手】"),s+='<li class="task-one" reward-type="'+n.data[r].reward_type+'"><div class="task-name float-left align-left"><a><em>'+n.data[r].task_name+'</em><span class="cf76a58">'+o+'</span></a><span class="task-descript">'+n.data[r].description+'<em></em></span></div><div class="task-number float-left"><span>'+n.data[r].current_process+"</span>/"+n.data[r].task_count+'</div><p class="task-gift float-left">'+n.data[r].task_reward+"</p>",3==n.data[r].finished_status?s+='<a class="task-go float-left bcF76A58 js-receiv-reward" href="javascript:void(0)" reward-type="'+n.data[r].reward_type+'" task-code="'+n.data[r].task_code+'">领取奖励</a></li>':1==n.data[r].finished_status?s+='<a class="task-go float-left bcCFD8DD" href="javascript:void(0)">已完成</a></li>':2==n.data[r].finished_status&&(s+='<a class="task-go float-left bcffd254 js-to-do-task" href="javascript:void(0);" data-href="'+n.data[r].task_url+'" >前往任务</a></li>')}$("#js-all-task").empty().append(s),loadingState=!0,showLoading("#js-task-content",loadingState),$(".task-one").delegate("a.js-to-do-task","click",function(){$(".task-contain").hide(),$(".black-bg").hide();var t=$(this).attr("data-href");window.location.href=t}),showDescript(),receivReward()}function getRewardData(){var t=5,a=!1;showLoading("#js-my-reward",a),$.ajax({url:"/task/finished/",type:"get",datatype:"json",success:function(a){"ok"==a.status&&(growRewardHtml(1,5,a),$(".js-reward-page").createPage({pageCount:Math.ceil(a.finished_count/t),current:1,backFn:function(t){var e=!1;showLoading("#js-my-reward",e),growRewardHtml(t,5,a)}}))}})}function dealDate(t){var a=new Date(t),e=a.getFullYear().toString(),s=(a.getMonth()+1).toString(),n=a.getDate().toString();return 1==s.length&&(s="0"+s),1==n.length&&(n="0"+n),e.toString()+"-"+s.toString()+"-"+n.toString()}function growRewardHtml(t,a,e){var s="",n=e,i=0;if(i=a*t<=n.data.length?a*t:n.data.length,n.data.length<1||null==n.data.length)s+='<li><div class="gift-null"><div class="gift-instrction">你还没有获得任何奖品哦<br>快去<a href="javascript:void(0)" class="c44b5e8" id="js-turn-to-task">所有任务</a>中和我一起做任务吧!</div></div></li>';else for(var s='<li><div class="task-gift-name float-left task-name-title-public align-left">任务名称</div><div class="task-gift-gift float-left task-name-title-public">奖品</div><div class="task-time-gift float-left task-name-title-public">领取时间</div><div class="task-time-gift float-left task-name-title-public">使用时间</div><div class="task-time-gift float-left task-name-title-public">过期时间</div></li>',r=a*(t-1);i>r;r++){var o="",l=n.data[r].reward_time,c=n.data[r].coupon_used_time,d=n.data[r].reward_due_time;l=null==l?"-":dealDate(parseInt(l.$date)),c=null==c?"-":dealDate(c.$date),d=null==d?"-":dealDate(d.$date),1==n.data[r].task_type&&(o+="【新手】"),s+='<li class="task-one"><div class="task-gift-name task-name float-left align-left"><a><em>'+n.data[r].task_name+'</em><span class="cf76a58">'+o+'</span></a><span class="task-descript">'+n.data[r].description+'<em></em></span></div><p class="task-gift-gift task-gift float-left">'+n.data[r].task_reward+'</p><p class="task-time-gift float-left c999999">'+l+'</p><p class="task-time-gift float-left c999999">'+c+'</p><p class="task-time-gift float-left cf76a58">'+d+"</p></li>"}$("#js-my-reward").empty().append(s),loadingState=!0,showLoading("#js-task-content",loadingState),$(".gift-instrction").delegate("a#js-turn-to-task","click",function(){$(".js-my-gift").removeClass("task-tab-current").siblings("a").addClass("task-tab-current"),$(".task-slide-contain").hide().eq(0).show()}),showDescript()}function showDescript(){$(".task-name").delegate("a","mouseover",function(){$(".task-descript").hide(),$(this).siblings(".task-descript").fadeIn(300),$(".task-descript").on("mouseout",function(){$(this).hide()})})}function receivReward(){$(".task-one").delegate("a.js-receiv-reward","click",function(){var t=$(this),a=t.attr("reward-type"),e=t.attr("task-code"),s=t.siblings(".task-gift").text(),n=!1;if(showLoading("#js-all-task",n),5==a){var i="."+reward[4].templateClass;$("#js-task-content").hide(),$("#js-reward-content").show(),$(i).show().siblings().hide(),$(".js-task-reward").text(s),getAdress(),submitAddress(e)}else 5!=a&&receiveAjax(e,a,s)})}function receiveAjax(t,a,e){$.ajax({url:"/task/receive_reward/",type:"POST",datatype:"json",data:{task_data:t},headers:{"X-CSRFToken":getCookie("csrftoken")},success:function(t){var s=!0;if(showLoading("#js-all-task",s),$("#js-task-content").hide(),$("#js-reward-content").show(),"ok"==t.status){for(var n=0,i=reward.length;i>n;n++)if(a==reward[n].taskType){var r="."+reward[n].templateClass;$(r).show().siblings().hide(),$(".js-task-reward").text(e);break}}else if("error"==t.status&&"weixin bind required"==t.msg){var r="."+reward[3].templateClass_error;$(r).show().siblings().hide(),$(".js-task-reward").text(e)}}})}function closeTask(){var t=getLocalData("no-tip");"block"==$("#js-task-tip").css("display")&&($("#js-task-tip").hide(),$(".task-close-tip").show()),("block"==$("#js-task-content").css("display")||"block"==$("#js-reward-content").css("display"))&&(t?t&&($(".task-contain").hide(),$(".black-bg").hide()):($(".task-contain").hide(),$(".task-close-tip").show()))}function getAdress(){$.ajax({url:"/task/address/",type:"get",datatype:"json",success:function(t){$("#js-task-reward-name").prop("value",t.name),$("#js-task-provice").prop("value",t.province),$("#js-task-city").prop("value",t.city),$("#js-task-street").prop("value",t.city)}})}function submitAddress(t){$("#js-submit-task-form").click(function(){var a=$("#js-task-reward-name").prop("value"),e=$("#js-task-provice").prop("value"),s=$("#js-task-city").prop("value"),n=$("#js-task-street").prop("value"),i=!0;if(0==a.length&&($("#js-task-reward-name").siblings("span.task-error-tip").show(),i=!1),(0==e.length||0==s.length)&&($("#js-task-city").siblings("span.task-error-tip").show(),i=!1),0==n.length&&($("#js-task-street").siblings("span.task-error-tip").show(),i=!1),i){var r=!1;showLoading(".gift-real-gift",r),$.ajax({url:"/task/address/",type:"POST",datatype:"json",data:{name:a,province:e,city:s,street:n},headers:{"X-CSRFToken":getCookie("csrftoken")},success:function(a){if("ok"==a.status){var e=!0;showLoading(".gift-real-gift",e),$(".submit-sucess").show(),$(".gift-real-gift").hide(),$.ajax({url:"/task/receive_reward/",type:"POST",datatype:"json",data:{task_data:t},headers:{"X-CSRFToken":getCookie("csrftoken")},success:function(t){}})}}})}})}!function(t){var a={init:function(t,e){return function(){a.fillHtml(t,e),a.bindEvent(t,e)}()},fillHtml:function(t,a){return function(){if(t.empty(),a.pageCount>1){var e="";e+=a.current>1?'<a href="javascript:;" class="prev-page noselect">&nbsp;</a>':'<a class="prev-page-disabled noselect">&nbsp;</a>',1!=a.current&&a.current>=4&&4!=a.pageCount&&(e+='<a href="javascript:;" class="page-num noselect">1</a>'),a.current-2>2&&a.current<=a.pageCount&&a.pageCount>5&&(e+="<span>...</span>");var s=a.current-2,n=a.current+2;for((s>1&&a.current<4||1==a.current)&&n++,a.current>a.pageCount-4&&a.current>=a.pageCount&&s--;n>=s;s++)s<=a.pageCount&&s>=1&&(e+=s!=a.current?'<a href="javascript:;" class="page-num noselect">'+s+"</a>":'<span class="current">'+s+"</span>");a.current+2<a.pageCount-1&&a.current>=1&&a.pageCount>5&&(e+="<span>...</span>"),a.current!=a.pageCount&&a.current<a.pageCount-2&&4!=a.pageCount&&(e+='<a href="javascript:;" class="page-num noselect">'+a.pageCount+"</a>"),e+=a.current<a.pageCount?'<a href="javascript:;" class="next-page noselect">&nbsp;</a>':'<a class="next-page-disabled noselect">&nbsp;</a>',t.append(e)}}()},bindEvent:function(e,s){return function(){e.off("click","a.page-num"),e.on("click","a.page-num",function(){var n=parseInt(t(this).text());a.fillHtml(e,{current:n,pageCount:s.pageCount}),"function"==typeof s.backFn&&s.backFn(n)}),e.off("click","a.prev-page"),e.on("click","a.prev-page",function(){var t=parseInt(e.children("span.current").text());a.fillHtml(e,{current:t-1,pageCount:s.pageCount}),"function"==typeof s.backFn&&s.backFn(t-1)}),e.off("click","a.next-page"),e.on("click","a.next-page",function(){var t=parseInt(e.children("span.current").text());a.fillHtml(e,{current:t+1,pageCount:s.pageCount}),"function"==typeof s.backFn&&s.backFn(t+1)})}()}};t.fn.createPage=function(e){var s=t.extend({pageCount:1,current:1,backFn:function(){}},e);a.init(this,s)}}(jQuery);var ualert=0,urgent_alert=document.getElementById("urgent_alert");null!=urgent_alert&&setInterval(function(){urgent_alert.style.left=ualert+"px",ualert-=1,-1600>ualert&&(ualert=500)},20);var reward=[{taskType:1,templateClass:"gift-pindian"},{taskType:2,templateClass:"gift-gold"},{taskType:3,templateClass:"gift-juan"},{taskType:4,templateClass:"gift-hongbao",templateClass_error:"gift-hongbao-error"},{taskType:5,templateClass:"gift-real-gift"}],getCookie=function(t){var a=document.cookie.match("(^|;) ?"+t+"=([^;]*)(;|$)");return a?a[2]:null};getTaskState();var windowWidth=$(window).width(),windowHeight=$(window).height();if($("#js-task-content,#js-reward-content").css({left:(windowWidth-600)/2,top:(windowHeight-550)/2}),$(".js-task-tip-contain").css({left:(windowWidth-600)/2,top:(windowHeight-400)/2}),$(".task-close-tip").css({left:(windowWidth-600)/2,top:(windowHeight-200)/2}),window.location.href.match("feed/feedFrequency")){var stateHtml='<div class="task-state-parent"><div class="task-state task-state-undo bd-trace" id="js-task-state" trace-title="任务系统"></div></div>',taskStateLeft=(windowWidth-1140)/2+160+"px";$("#js-task-state").remove(),$("body").append(stateHtml),$("#js-task-state").css("right",taskStateLeft)}else{var taskStateLeft=(windowWidth-1140)/2+160+"px";$("#js-task-state").css("right",taskStateLeft)}$(".task-state-parent").delegate("div.task-state","click",function(){setLocalData("task_tip","ture"),getTaskData()}),$(".black-bg").on("click",function(){closeTask()}),$(".js-close-task").click(function(){closeTask()}),$(".task-start-confirm,.js-close-task-tip").click(function(){setLocalData("no-tip","ture"),$(".task-close-tip").hide(),$(".black-bg").hide()}),setInterval('AutoScroll(".task-notice-one","-32px")',3e3),setInterval('AutoScroll(".task-notice-two","-32px")',3e3),setInterval('AutoScroll(".task-notice-three","-32px")',3e3),$(".task-tab a").click(function(){var t=$(this).index();$(this).addClass("task-tab-current").siblings("a").removeClass("task-tab-current"),$(".task-slide-contain").hide().eq(t).show(),$(this).hasClass("js-my-gift")&&getRewardData()}),$(".js-task-return").click(function(){"block"==$(".gift-real-gift").css("display")?($("#js-task-content").show(),$("#js-reward-content").hide()):($("#js-task-content").show(),$("#js-reward-content").hide(),getTaskData(),getTaskState())}),$(".js-confirm").click(function(){$("#js-task-content").show(),$("#js-reward-content").hide(),getTaskData(),getTaskState()}),function(){var t=getLocalData("task_tip");t||($(".js-task-tip-contain").show(),$(".black-bg").show(),$.ajax({url:"/task/",type:"get",datatype:"json",success:function(t){"ok"==t.status&&fillSpeaker(t)}}),$(".js-start-task").click(function(){setLocalData("task_tip","ture"),$(".js-task-tip-contain").hide(),$("#js-task-content").show(),getTaskData()}))}();