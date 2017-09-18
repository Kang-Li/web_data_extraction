odoo.define('web_data_extraction', function (require) {
"use strict";

var core = require('web.core');
var ajax = require('web.ajax');
var Widget = require('web.Widget');

var Dashboard = Widget.extend({
    template: 'WebDataExtractionMain',

    init: function(parent, data){
        return this._super.apply(this, arguments);
    },

    start: function(){
        var self = this
        this.$("#extract_setup").hide()
        this.$("input[name='target_url']").bind('keyup',function(event){
            if(event.keyCode==13)
                self.target_click()
        })

        this.$el.on('click', '#target_click', function (event) {
            self.target_click()
         });

        this.$el.on('click', '#extract_click', function (event) {
            self.extract_click()
         });

        return true;
    },

    target_click: function() {
        var url=this.$el.find("input[name='target_url']").val()
        url=$.trim(url)
        if(url != '') {
            if(url.indexOf("http") != 0)
                url = "http://" + url
            var ifr = this.$('#web_data_extraction_iframe')
            var input_url = this.$('#input_url')
            var extract_setup = this.$("#extract_setup")
            var url2 = window.location.protocol + "//" + window.location.host
            ajax.jsonRpc('/web_data_extraction/target_url', 'call', {
                target_url: url,
                source_url: url2
            }).then(function (results) {
                ifr.attr("srcdoc",results['html'])
                input_url.remove()
                extract_setup.show()
            })
        }
    },

    extract_click: function() {
        var ifr = this.$('#web_data_extraction_iframe')
        alert(ifr.contents().find("#fc").html())
    }


});



core.action_registry.add('web_data_extraction.main', Dashboard);

return {
    Dashboard: Dashboard,
};

});
