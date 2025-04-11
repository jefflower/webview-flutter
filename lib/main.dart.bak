import 'package:flutter/material.dart';
import 'package:flutter_inappwebview/flutter_inappwebview.dart';
import 'dart:io';

Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();

  // 配置 WebView
  if (Platform.isAndroid) {
    await AndroidInAppWebViewController.setWebContentsDebuggingEnabled(true);
  }

  // 捕获全局错误
  FlutterError.onError = (FlutterErrorDetails details) {
    FlutterError.presentError(details);
    debugPrint('Flutter Error: ${details.toString()}');
  };

  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: '叫号大屏@MicroHis',
      debugShowCheckedModeBanner: false, // 移除调试标记
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: const WebViewPage(),
    );
  }
}

class WebViewPage extends StatefulWidget {
  const WebViewPage({super.key});

  @override
  State<WebViewPage> createState() => _WebViewPageState();
}

class _WebViewPageState extends State<WebViewPage> {
  final String initialUrl = 'https://www.baidu.com';
  double progress = 0;
  String? errorMessage;
  bool isLoading = true;

  @override
  Widget build(BuildContext context) {
    return WillPopScope(
      onWillPop: () async {
        // 处理返回按钮
        if (webViewController != null) {
          if (await webViewController!.canGoBack()) {
            webViewController!.goBack();
            return false;
          }
        }
        return true;
      },
      child: Scaffold(
        appBar: AppBar(
          title: const Text('叫号大屏@MicroHis'),
          actions: [
            IconButton(
              icon: const Icon(Icons.refresh),
              onPressed: () {
                webViewController?.reload();
              },
            ),
          ],
        ),
        body: Stack(
          children: [
            Column(
              children: [
                if (progress < 1.0) LinearProgressIndicator(value: progress),
                if (errorMessage != null)
                  Container(
                    padding: const EdgeInsets.all(16),
                    color: Colors.red[100],
                    child: Text(
                      '加载错误: $errorMessage',
                      style: const TextStyle(color: Colors.red),
                    ),
                  ),
                Expanded(
                  child: InAppWebView(
                    initialUrlRequest: URLRequest(url: WebUri(initialUrl)),
                    initialOptions: InAppWebViewGroupOptions(
                      crossPlatform: InAppWebViewOptions(
                        useShouldOverrideUrlLoading: true,
                        mediaPlaybackRequiresUserGesture: false,
                        javaScriptEnabled: true,
                        javaScriptCanOpenWindowsAutomatically: true,
                        userAgent:
                            'Mozilla/5.0 (Linux; Android 5.7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
                      ),
                      android: AndroidInAppWebViewOptions(
                        useHybridComposition: true,
                        mixedContentMode:
                            AndroidMixedContentMode.MIXED_CONTENT_ALWAYS_ALLOW,
                      ),
                    ),
                    onWebViewCreated: (controller) {
                      webViewController = controller;
                    },
                    onLoadStart: (controller, url) {
                      setState(() {
                        errorMessage = null;
                        isLoading = true;
                      });
                    },
                    onLoadStop: (controller, url) {
                      setState(() {
                        isLoading = false;
                      });
                    },
                    onProgressChanged: (controller, progress) {
                      setState(() {
                        this.progress = progress / 100;
                      });
                    },
                    onLoadError: (controller, url, code, message) {
                      setState(() {
                        errorMessage = message;
                        isLoading = false;
                      });
                    },
                    onLoadHttpError:
                        (controller, url, statusCode, description) {
                      setState(() {
                        errorMessage = 'HTTP Error $statusCode: $description';
                        isLoading = false;
                      });
                    },
                    androidOnPermissionRequest:
                        (controller, origin, resources) async {
                      return PermissionRequestResponse(
                        resources: resources,
                        action: PermissionRequestResponseAction.GRANT,
                      );
                    },
                  ),
                ),
              ],
            ),
            if (isLoading)
              const Center(
                child: CircularProgressIndicator(),
              ),
          ],
        ),
      ),
    );
  }

  InAppWebViewController? webViewController;

  @override
  void dispose() {
    webViewController?.dispose();
    super.dispose();
  }
}
