{
  'includes': [
    '../../build/common.gypi',
  ],
  'targets': [
    {
      'target_name': 'activex_shim',
      'type': 'static_library',
      'dependencies': [
        '../../base/base.gyp:base',
        '../../third_party/npapi/npapi.gyp:npapi',
        '../../googleurl/build/googleurl.gyp:googleurl',
      ],
      'sources': [
        'activex_plugin.cc',
        'activex_plugin.h',
        'activex_shared.cc',
        'activex_shared.h',
        'activex_util.cc',
        'activex_util.h',
        'dispatch_object.cc',
        'dispatch_object.h',
        'ihtmldocument_impl.h',
        'iwebbrowser_impl.h',
        'npn_scripting.cc',
        'npn_scripting.h',
        'npp_impl.cc',
        'npp_impl.h',
        'README',
        'web_activex_container.cc',
        'web_activex_container.h',
        'web_activex_site.cc',
        'web_activex_site.h',
      ],
      'libraries': [
        'urlmon.lib',
      ],
    },
  ],
}
