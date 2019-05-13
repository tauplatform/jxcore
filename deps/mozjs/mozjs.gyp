{
  'targets': [
    {
      'target_name': 'embedjs_py',
      'type': 'none',
      'toolsets': ['combine'],
    },
    {
      'target_name': 'mozjs',
      'type': '<(library)',
    
      'include_dirs': [
        'incs/',
        'incs/icu/source/common',
        'incs/mozilla/double-conversion',
        'src',
        '<(SHARED_INTERMEDIATE_DIR)',
      ],
      
      'sources': [ 
       'incs/mozilla/Char16.h',
       'incs/mozilla/double-conversion/bignum.cc',
       'incs/mozilla/double-conversion/bignum-dtoa.cc',
       'incs/mozilla/double-conversion/cached-powers.cc',
       'incs/mozilla/double-conversion/diy-fp.cc',
       'incs/mozilla/double-conversion/double-conversion.cc',
       'incs/mozilla/double-conversion/fast-dtoa.cc',
       'incs/mozilla/double-conversion/fixed-dtoa.cc',
       'incs/mozilla/double-conversion/strtod.cc',
       'incs/mozilla/Poison.cpp', 
       'incs/mozilla/SHA1.cpp', 
       'incs/mozilla/Compression__.cpp',
       'incs/mozilla/FloatingPoint.cpp',
       'incs/mozilla/HashFunctions.cpp',
       'incs/mozilla/TaggedAnonymousMemory.cpp',
       
       'src/frontend/Parser.cpp',
       'src/jsarray.cpp',
       'src/jsatom.cpp',
       'src/jsmath.cpp',
       'src/jsutil.cpp',
  
       'src/asmjs/AsmJSFrameIterator.cpp',
       'src/asmjs/AsmJSLink.cpp',
       'src/asmjs/AsmJSModule.cpp',
       'src/asmjs/AsmJSSignalHandlers.cpp',
       'src/asmjs/AsmJSValidate.cpp',
       
       'src/builtin/Eval.cpp',
       'src/builtin/Intl.cpp',
       'src/builtin/MapObject.cpp',
       'src/builtin/Object.cpp',
       'src/builtin/RegExp.cpp',
       'src/builtin/Profilers.cpp',
       'src/builtin/SIMD.cpp',
       'src/builtin/TestingFunctions.cpp',
       'src/builtin/TypedObject.cpp',
       'src/builtin/SymbolObject.cpp',
       'src/builtin/WeakSetObject.cpp',
       'src/devtools/sharkctl.cpp',
       'src/ds/LifoAlloc.cpp',
       'src/frontend/BytecodeCompiler.cpp',
       'src/frontend/BytecodeEmitter.cpp',
       'src/frontend/FoldConstants.cpp',
       'src/frontend/NameFunctions.cpp',
       'src/frontend/ParseMaps.cpp',
       'src/frontend/ParseNode.cpp',
       'src/frontend/TokenStream.cpp',
       'src/gc/ForkJoinNursery.cpp',
       'src/gc/GCTrace.cpp',
       'src/gc/Barrier.cpp',
       'src/gc/Iteration.cpp',
       'src/gc/Marking.cpp',
       'src/gc/Memory.cpp',
       'src/gc/Nursery.cpp',
       'src/gc/RootMarking.cpp',
       'src/gc/Statistics.cpp',
       'src/gc/StoreBuffer.cpp',
       'src/gc/Tracer.cpp',
       'src/gc/Verifier.cpp',
       'src/gc/Zone.cpp',
       
       'src/irregexp/NativeRegExpMacroAssembler.cpp',
       'src/irregexp/RegExpAST.cpp',
       'src/irregexp/RegExpEngine.cpp',
       'src/irregexp/RegExpInterpreter.cpp',
       'src/irregexp/RegExpMacroAssembler.cpp',
       'src/irregexp/RegExpParser.cpp',
       'src/irregexp/RegExpStack.cpp',
       'src/jit/AliasAnalysis.cpp',
       'src/jit/BacktrackingAllocator.cpp',
       'src/jit/Bailouts.cpp',
       'src/jit/BaselineBailouts.cpp',
       'src/jit/BaselineCompiler.cpp',
       'src/jit/BaselineDebugModeOSR.cpp',
       'src/jit/BaselineFrame.cpp',
       'src/jit/BaselineFrameInfo.cpp',
       'src/jit/BaselineIC.cpp',
       'src/jit/BaselineInspector.cpp',
       'src/jit/BaselineJIT.cpp',
       'src/jit/BitSet.cpp',
       'src/jit/BytecodeAnalysis.cpp',
       'src/jit/C1Spewer.cpp',
       'src/jit/CodeGenerator.cpp',
       'src/jit/CompileWrappers.cpp',
       'src/jit/EdgeCaseAnalysis.cpp',
       'src/jit/EffectiveAddressAnalysis.cpp',
       'src/jit/ExecutableAllocator.cpp',
       'src/jit/Ion.cpp',
       'src/jit/IonAnalysis.cpp',
       'src/jit/IonBuilder.cpp',
       'src/jit/IonCaches.cpp',
       'src/jit/IonFrames.cpp',
       'src/jit/IonMacroAssembler.cpp',
       'src/jit/IonOptimizationLevels.cpp',
       'src/jit/IonSpewer.cpp',
       'src/jit/JitcodeMap.cpp',
       'src/jit/JitOptions.cpp',
       'src/jit/JSONSpewer.cpp',
       'src/jit/LICM.cpp',
       'src/jit/LinearScan.cpp',
       'src/jit/LIR.cpp',
       'src/jit/LiveRangeAllocator.cpp',
       'src/jit/LoopUnroller.cpp',
       'src/jit/Lowering.cpp',
       'src/jit/MCallOptimize.cpp',
       'src/jit/MIR.cpp',
       'src/jit/MIRGraph.cpp',
       'src/jit/MoveResolver.cpp',
       'src/jit/ParallelFunctions.cpp',
       'src/jit/ParallelSafetyAnalysis.cpp',
       'src/jit/PerfSpewer.cpp',
       'src/jit/RangeAnalysis.cpp',
       'src/jit/Recover.cpp',
       'src/jit/RegisterAllocator.cpp',
       'src/jit/RematerializedFrame.cpp',
       'src/jit/Safepoints.cpp',
       'src/jit/ScalarReplacement.cpp',
       'src/jit/shared/BaselineCompiler-shared.cpp',
       'src/jit/shared/CodeGenerator-shared.cpp',
       'src/jit/shared/Lowering-shared.cpp',
       'src/jit/Snapshots.cpp',
       'src/jit/StupidAllocator.cpp',
       'src/jit/TypedObjectPrediction.cpp',
       'src/jit/TypePolicy.cpp',
       'src/jit/UnreachableCodeElimination.cpp',
       'src/jit/ValueNumbering.cpp',
       'src/jit/VMFunctions.cpp',
       
       'src/jsalloc.cpp',
       'src/jsapi.cpp',
       'src/jsbool.cpp',
       'src/jscntxt.cpp',
       'src/jscompartment.cpp',
       'src/jscrashreport.cpp',
       'src/jsdate.cpp',
       'src/jsdtoa.cpp',
       'src/jsexn.cpp',
       'src/jsfriendapi.cpp',
       'src/jsfun.cpp',
       'src/jsgc.cpp',
       'src/jsinfer.cpp',
       'src/jsiter.cpp',
       'src/jsnativestack.cpp',
       'src/jsnum.cpp',
       'src/jsobj.cpp',
       'src/json.cpp',
       'src/jsonparser.cpp',
       'src/jsopcode.cpp',
       'src/jsprf.cpp',
       'src/jspropertytree.cpp',
       'src/jsproxy.cpp',
       'src/jsreflect.cpp',
       'src/jsscript.cpp',
       'src/jsstr.cpp',
       'src/jswatchpoint.cpp',
       'src/jsweakmap.cpp',
       'src/jswrapper.cpp',
       'src/perf/jsperf.cpp',
       'src/prmjtime.cpp',
       'src/vm/ArgumentsObject.cpp',
       'src/vm/CallNonGenericMethod.cpp',
       'src/vm/CharacterEncoding.cpp',
       'src/vm/DateTime.cpp',
       'src/vm/Debugger.cpp',
       'src/vm/DebuggerMemory.cpp',
       'src/vm/ErrorObject.cpp',
       'src/vm/ForkJoin.cpp',
       'src/vm/GlobalObject.cpp',
       'src/vm/HelperThreads.cpp',
       'src/vm/Id.cpp',
       'src/vm/Interpreter.cpp',
       'src/vm/MemoryMetrics.cpp',
       'src/vm/Monitor.cpp',
       'src/vm/ObjectImpl.cpp',
       'src/vm/OldDebugAPI.cpp',
       'src/vm/Probes.cpp',
       'src/vm/PropertyKey.cpp',
       'src/vm/ProxyObject.cpp',
       'src/vm/RegExpObject.cpp',
       'src/vm/RegExpStatics.cpp',
       'src/vm/Runtime.cpp',
       'src/vm/SavedStacks.cpp',
       'src/vm/ScopeObject.cpp',
       'src/vm/SelfHosting.cpp',
       'src/vm/Shape.cpp',
       'src/vm/SPSProfiler.cpp',
       'src/vm/Stack.cpp',
       'src/vm/String.cpp',
       'src/vm/StringBuffer.cpp',
       'src/vm/StructuredClone.cpp',
       'src/vm/Symbol.cpp',
       'src/vm/UbiNode.cpp',
       'src/vm/ThreadPool.cpp',
       'src/vm/TypedArrayObject.cpp',
       'src/vm/Unicode.cpp',
       'src/vm/Value.cpp',
       'src/vm/Xdr.cpp',
       'src/vm/SharedArrayObject.cpp',
       'src/vm/PIC.cpp',
       'src/vm/Compression.cpp',
       'src/vm/ArrayBufferObject.cpp',
       'src/vm/WeakMapPtr.cpp',
      ],
      
      'defines': [
        'DISABLE_SHARED_JS=1',
        'EXPORT_JS_API=1',
        'JS_DEFAULT_JITREPORT_GRANULARITY=3',   # JITREPORT_GRANULARITY_OP
        'JSGC_INCREMENTAL=1',
        'IMPL_MFBT=1',
        'MOZILLA_VERSION="340"',
        'STATIC_JS_API=1',
      ],
      'configurations': {
        'Debug': {
          'defines': [ 'JS_DEBUG' ],
          'conditions': [
            [ 'OS == "linux" and target_arch == "x64"', {
              'cflags_cc': [ '-fpermissive' ],
              }],
          ],
        },
        'Release': {
          'defines': ['NDEBUG'],
        },
      },  
      'dependencies': [ '../zlib/zlib.gyp:zlib' ],
      'conditions': 
      [ 
        ['uclibc_defined == 1', {
          'defines':['POSIX_UCLIBC_DEFINED'],
        }], 
        ['target_arch in "arm armv7 armv7s"', {
          'defines': [ 'WTF_CPU_ARM_TRADITIONAL', 'JS_NUNBOX32', 'JS_CPU_ARM=1' ],
        }],
        ['target_arch=="arm64"', {
          'defines': [ 'WTF_CPU_ARM_TRADITIONAL', 'JS_PUNBOX64', 'JS_CPU_ARM=1' ],
        }],
        ['target_arch in "arm armv7 arm64 armv7s"', {
            'conditions':[
              ['OS in "win ios" or target_arch=="arm64"', {
                'sources':[
                  'src/jit/none/Trampoline-none.cpp'   # ION DISABLED
                ],
                'defines':[
                  'JS_CODEGEN_NONE=1' # Interpreter only
                ]
              },
              { #ARM JIT
                'sources':[
                  'src/jit/arm/Architecture-arm.cpp',
                  'src/jit/arm/Assembler-arm.cpp',
                  'src/jit/arm/Bailouts-arm.cpp',
                  'src/jit/arm/BaselineCompiler-arm.cpp',
                  'src/jit/arm/BaselineIC-arm.cpp',
                  'src/jit/arm/CodeGenerator-arm.cpp',
                  'src/jit/arm/Lowering-arm.cpp',
                  'src/jit/arm/MacroAssembler-arm.cpp',
                  'src/jit/arm/MoveEmitter-arm.cpp',
                  'src/jit/arm/Trampoline-arm.cpp',
                ],
                'defines':[
                  'JS_CODEGEN_ARM=1'
                ]
              }]
            ]
        }],
        ['target_arch in "mipsel mips"', {
          'sources':[
            'src/jit/none/Trampoline-none.cpp'   # ION DISABLED
          ],
          'defines' : [ 'JS_CODEGEN_NONE', 'JS_NUNBOX32', 'JS_CPU_MIPS' ]
        }],
        ['target_arch in "x64 ia32"', {
          'defines': ['HAVE_VA_LIST_AS_ARRAY=1']
        }],
        ['node_win_onecore==1', {
          'defines': [
            '_WIN32_WINNT=0x0A00',  # WIN10
          ]
        }],
        ['target_arch=="x64"', {
          'defines':[ 'JS_PUNBOX64', 'JS_CPU_X64=1' ],
          'conditions':[
          ['OS=="ios" or node_win_onecore==1', {
            'sources':[
              'src/jit/none/Trampoline-none.cpp'   # ION DISABLED
            ],
            'defines':[
              'JS_CODEGEN_NONE=1' # Interpreter only
            ]
          },{ #X64 JIT
              'sources':[
                'src/jit/x64/Assembler-x64.cpp',
                'src/jit/x64/Bailouts-x64.cpp',
                'src/jit/x64/BaselineCompiler-x64.cpp',
                'src/jit/x64/BaselineIC-x64.cpp',
                'src/jit/x64/CodeGenerator-x64.cpp',
                'src/jit/x64/Lowering-x64.cpp',
                'src/jit/x64/MacroAssembler-x64.cpp',
                'src/jit/x64/Trampoline-x64.cpp',
                #commons
                'src/jit/shared/Assembler-x86-shared.cpp',
                'src/jit/shared/BaselineCompiler-x86-shared.cpp',
                'src/jit/shared/BaselineIC-x86-shared.cpp',
                'src/jit/shared/CodeGenerator-x86-shared.cpp',
                'src/jit/shared/Lowering-x86-shared.cpp',
                'src/jit/shared/MacroAssembler-x86-shared.cpp',
                'src/jit/shared/MoveEmitter-x86-shared.cpp',
              ],
              'defines':[
                'JS_CODEGEN_X64=1'
              ]
            }]
          ],
        }],
        ['target_arch=="ia32"', {
            'defines':[ 'JS_NUNBOX32', 'JS_CPU_X86=1' ],
            'conditions':[
              ['OS=="ios" or node_win_onecore==1', {
                'sources':[
                  'src/jit/none/Trampoline-none.cpp'   # ION DISABLED
                ],
                'defines':[
                  'JS_CODEGEN_NONE=1' # Interpreter only
                ]
              },
              { #X86 JIT
                'sources':[
                  'src/jit/x86/Assembler-x86.cpp',
                  'src/jit/x86/Bailouts-x86.cpp',
                  'src/jit/x86/BaselineCompiler-x86.cpp',
                  'src/jit/x86/BaselineIC-x86.cpp',
                  'src/jit/x86/CodeGenerator-x86.cpp',
                  'src/jit/x86/Lowering-x86.cpp',
                  'src/jit/x86/MacroAssembler-x86.cpp',
                  'src/jit/x86/Trampoline-x86.cpp',
                  #commons
                  'src/jit/shared/Assembler-x86-shared.cpp',
                  'src/jit/shared/BaselineCompiler-x86-shared.cpp',
                  'src/jit/shared/BaselineIC-x86-shared.cpp',
                  'src/jit/shared/CodeGenerator-x86-shared.cpp',
                  'src/jit/shared/Lowering-x86-shared.cpp',
                  'src/jit/shared/MacroAssembler-x86-shared.cpp',
                  'src/jit/shared/MoveEmitter-x86-shared.cpp',
                ],
                'defines':[
                  'JS_CODEGEN_X86=1'
                ]
              }]
            ],
        }],
        ['OS=="mac"', {
          'xcode_settings': {
            'MACOSX_DEPLOYMENT_TARGET': '10.7', # -mmacosx-version-min=10.7 
          }
        }],
        ['OS=="mac" or OS=="ios"', {
          'sources': [
            'src/perf/pm_stub.cpp',
          ],
          'defines': [
            'XP_MACOSX=1',
            'DARWIN=1',
            'JS_HAVE_MACHINE_ENDIAN_H=1',
          ],
          'xcode_settings': {
            'OTHER_CPLUSPLUSFLAGS' : ['-std=c++11', '-stdlib=libc++',
              '-Wno-mismatched-tags', '-Wno-missing-field-initializers',
              '-Wno-unused-private-field', '-Wno-invalid-offsetof', '-Wno-ignored-qualifiers'],
            'OTHER_CFLAGS' : [],
          }
        }],
      ['OS=="ios"', {
        'xcode_settings': {
          'ALWAYS_SEARCH_USER_PATHS': 'NO',
          'GCC_CW_ASM_SYNTAX': 'NO',                # No -fasm-blocks
          'GCC_DYNAMIC_NO_PIC': 'NO',               # No -mdynamic-no-pic
                                                    # (Equivalent to -fPIC)
          'GCC_ENABLE_CPP_EXCEPTIONS': 'NO',        # -fno-exceptions
          'GCC_ENABLE_CPP_RTTI': 'NO',              # -fno-rtti
          'GCC_ENABLE_PASCAL_STRINGS': 'NO',        # No -mpascal-strings
          'GCC_THREADSAFE_STATICS': 'NO',           # -fno-threadsafe-statics
          'PREBINDING': 'NO',                       # No -Wl,-prebind
          'EMBED_BITCODE': 'YES',
          'IPHONEOS_DEPLOYMENT_TARGET': '8.0',
          'CLANG_CXX_LIBRARY': 'libc++',
          'GCC_GENERATE_DEBUGGING_SYMBOLS': 'NO',
          
          'USE_HEADERMAP': 'NO',
          'OTHER_CFLAGS': [
            '-fno-strict-aliasing',
            '-fno-standalone-debug'
          ],
          'OTHER_CPLUSPLUSFLAGS': [
            '-fno-strict-aliasing',
            '-fno-standalone-debug'
          ],
          'OTHER_LDFLAGS': [
            '-s'
          ],
          'WARNING_CFLAGS': [
            '-Wall',
            '-Wendif-labels',
            '-W',
            '-Wno-unused-parameter',
          ],
        },
        'defines':[ '__IOS__' ],
        'conditions': [
          ['target_arch=="ia32"', {
            'xcode_settings': {'ARCHS': ['i386']},
          }],
          ['target_arch=="x64"', {
            'xcode_settings': {'ARCHS': ['x86_64']},
          }],
          [ 'target_arch in "arm64 arm armv7s"', {
            'xcode_settings': {
              'OTHER_CFLAGS': [
                '-fembed-bitcode'
              ],
              'OTHER_CPLUSPLUSFLAGS': [
                '-fembed-bitcode'
              ],
            }
          }],
          [ 'target_arch=="arm64"', {
            'xcode_settings': {'ARCHS': ['arm64']},
          }],
          [ 'target_arch=="arm"', {
            'xcode_settings': {'ARCHS': ['armv7']},
          }],
          [ 'target_arch=="armv7s"', {
            'xcode_settings': {'ARCHS': ['armv7s']},
          }],
          [ 'target_arch=="x64" or target_arch=="ia32"', {
            'xcode_settings': { 'SDKROOT': 'iphonesimulator' },
          }, {
            'xcode_settings': { 'SDKROOT': 'iphoneos', 'ENABLE_BITCODE': 'YES'},
          }]
        ],
      }],
        [ 'OS!="ios" and OS!="android"', {
          'dependencies': [ './jskwgen.gyp:jskwgen' ],
        }],
        ['OS in "linux"', {
           'sources':[
             'src/perf/pm_linux.cpp',
           ],
        }],
        ['OS in "android bsd"', {
           'sources':[
             'src/perf/pm_stub.cpp',
           ],
        }],
        [ 'OS=="android"', {
          'defines': [
            'ANDROID'
          ],
          'ldflags': [ 'log', 'z', 'android' ],
          'cflags!': [
            '-pthread',
          ],
          'cflags': [
            '-fomit-frame-pointer',
            '-fno-rtti',
            '-ffunction-sections',
            '-funwind-tables',
            '-fstack-protector',
            '-fno-short-enums',
            '-finline-limit=64',
            '-O2',
          ],
        }],
        ['OS in "linux android freebsd"', {
           "cflags": [
             "-std=c++0x", '-D__STDC_LIMIT_MACROS',
             '-Wno-missing-field-initializers',
             '-Wno-invalid-offsetof', '-Wno-ignored-qualifiers', '-Wno-extra'
           ],
        }],
        ['OS=="freebsd"', {
          'ldflags': ['-pthread'],
          "defines": [
            "JS_HAVE_MACHINE_ENDIAN_H",
          ],
        }],
        ['OS in "linux android"', {
          'ldflags': ['dl'],
          "defines": [
             "JS_HAVE_ENDIAN_H",
           ],
        }],
        ['OS=="win"', {
           'defines': [ 'XP_WIN', '_CRT_RAND_S', 'WTF_COMPILER_MSVC' ],  
           'sources': [
             'src/perf/pm_stub.cpp',
             'src/jit/ExecutableAllocatorWin.cpp',
           ],
           'include_dirs': [
             'pre_built', 'incs/nss/nspr/pr/include',
           ],
           'dependencies': [ 'incs/nss/nss.gyp:nspr' ],
           'conditions':[
             ['target_arch=="x64"', {
               'defines':['_AMD64_']
             }, {
               'defines':['_X86_']
           }]
         ], 
         'msvs_settings': {
            'VCLibrarianTool': {
              'AdditionalDependencies': [
                'winmm.lib',
              ],
            }
          }
         },
         { #no WIN
           'cflags': [
             '-pthread'
           ],
           'defines': [ 'XP_UNIX', 'MOZ_CHAR16_IS_NOT_WCHAR', 'JS_POSIX_NSPR' ], 
           'sources': [
             'src/jit/ExecutableAllocatorPosix.cpp',
             'src/vm/PosixNSPR.cpp',
           ],
           'actions': [
           {
           'action_name': 'embed_js_py',
           'inputs': ['src/builtin/embedjs.py'],
           'outputs': [ #DO NOT CHANGE THE BELOW ORDER!!
             'src/builtin/Utilities.js',
             'src/builtin/TypedObject.js',
             'src/builtin/Array.js', 
             'src/builtin/Date.js', 
             'src/builtin/Object.js',
             'src/builtin/String.js',
             'src/builtin/Error.js', 
             'src/builtin/Intl.js', 
             'src/builtin/IntlData.js', 
             'src/builtin/Iterator.js',
             'src/builtin/Map.js',
             'src/builtin/Number.js', 
             'src/builtin/ParallelUtilities.js', 
             'src/builtin/Set.js',
             'src/builtin/WeakSet.js',
           ],
           'action': [
            'python',
            'src/builtin/embedjs.py',
            '<@(_inputs)',
            '-c "gcc" ',
            '-p -o ',
            '-sselfhosted.js',
            '-msrc/js.msg',
            '-o<(SHARED_INTERMEDIATE_DIR)/selfhosted.out.h',
            '<@(_outputs)'
           ],
         }]
       }]
     ]  
  }]
}
