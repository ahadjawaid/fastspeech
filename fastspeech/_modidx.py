# Autogenerated by nbdev

d = { 'settings': { 'branch': 'main',
                'doc_baseurl': '/fastspeech',
                'doc_host': 'https://ahadjawaid.github.io',
                'git_url': 'https://github.com/ahadjawaid/fastspeech',
                'lib_path': 'fastspeech'},
  'syms': { 'fastspeech.data': { 'fastspeech.data.TTSDataset': ('data.html#ttsdataset', 'fastspeech/data.py'),
                                 'fastspeech.data.TTSDataset.__getitem__': ('data.html#ttsdataset.__getitem__', 'fastspeech/data.py'),
                                 'fastspeech.data.TTSDataset.__init__': ('data.html#ttsdataset.__init__', 'fastspeech/data.py'),
                                 'fastspeech.data.TTSDataset.__len__': ('data.html#ttsdataset.__len__', 'fastspeech/data.py'),
                                 'fastspeech.data.collate_fn': ('data.html#collate_fn', 'fastspeech/data.py'),
                                 'fastspeech.data.compute_statistics': ('data.html#compute_statistics', 'fastspeech/data.py')},
            'fastspeech.loading': { 'fastspeech.loading.get_audio_files': ('loading.html#get_audio_files', 'fastspeech/loading.py'),
                                    'fastspeech.loading.get_phones_and_durations': ( 'loading.html#get_phones_and_durations',
                                                                                     'fastspeech/loading.py'),
                                    'fastspeech.loading.load_audio': ('loading.html#load_audio', 'fastspeech/loading.py'),
                                    'fastspeech.loading.load_tiers': ('loading.html#load_tiers', 'fastspeech/loading.py'),
                                    'fastspeech.loading.melspectrogram': ('loading.html#melspectrogram', 'fastspeech/loading.py'),
                                    'fastspeech.loading.replace_extension': ('loading.html#replace_extension', 'fastspeech/loading.py')},
            'fastspeech.modules': { 'fastspeech.modules.ConvNetwork': ('modules.html#convnetwork', 'fastspeech/modules.py'),
                                    'fastspeech.modules.ConvNetwork.__init__': ( 'modules.html#convnetwork.__init__',
                                                                                 'fastspeech/modules.py'),
                                    'fastspeech.modules.ConvNetwork.forward': ('modules.html#convnetwork.forward', 'fastspeech/modules.py'),
                                    'fastspeech.modules.DPConfig': ('modules.html#dpconfig', 'fastspeech/modules.py'),
                                    'fastspeech.modules.DPConfig.__init__': ('modules.html#dpconfig.__init__', 'fastspeech/modules.py'),
                                    'fastspeech.modules.DPConfig.build': ('modules.html#dpconfig.build', 'fastspeech/modules.py'),
                                    'fastspeech.modules.DurationPredictor': ('modules.html#durationpredictor', 'fastspeech/modules.py'),
                                    'fastspeech.modules.DurationPredictor.__init__': ( 'modules.html#durationpredictor.__init__',
                                                                                       'fastspeech/modules.py'),
                                    'fastspeech.modules.DurationPredictor.forward': ( 'modules.html#durationpredictor.forward',
                                                                                      'fastspeech/modules.py'),
                                    'fastspeech.modules.FFTConfig': ('modules.html#fftconfig', 'fastspeech/modules.py'),
                                    'fastspeech.modules.FFTConfig.__init__': ('modules.html#fftconfig.__init__', 'fastspeech/modules.py'),
                                    'fastspeech.modules.FFTConfig.build': ('modules.html#fftconfig.build', 'fastspeech/modules.py'),
                                    'fastspeech.modules.FastSpeech': ('modules.html#fastspeech', 'fastspeech/modules.py'),
                                    'fastspeech.modules.FastSpeech.__init__': ('modules.html#fastspeech.__init__', 'fastspeech/modules.py'),
                                    'fastspeech.modules.FastSpeech.forward': ('modules.html#fastspeech.forward', 'fastspeech/modules.py'),
                                    'fastspeech.modules.FeedForwardTransformer': ( 'modules.html#feedforwardtransformer',
                                                                                   'fastspeech/modules.py'),
                                    'fastspeech.modules.FeedForwardTransformer.__init__': ( 'modules.html#feedforwardtransformer.__init__',
                                                                                            'fastspeech/modules.py'),
                                    'fastspeech.modules.FeedForwardTransformer.forward': ( 'modules.html#feedforwardtransformer.forward',
                                                                                           'fastspeech/modules.py'),
                                    'fastspeech.modules.MultiHeadAttention': ('modules.html#multiheadattention', 'fastspeech/modules.py'),
                                    'fastspeech.modules.MultiHeadAttention.__init__': ( 'modules.html#multiheadattention.__init__',
                                                                                        'fastspeech/modules.py'),
                                    'fastspeech.modules.MultiHeadAttention.forward': ( 'modules.html#multiheadattention.forward',
                                                                                       'fastspeech/modules.py'),
                                    'fastspeech.modules.get_positional_embeddings': ( 'modules.html#get_positional_embeddings',
                                                                                      'fastspeech/modules.py'),
                                    'fastspeech.modules.length_regulator': ('modules.html#length_regulator', 'fastspeech/modules.py')},
            'fastspeech.preprocess': { 'fastspeech.preprocess.MinMaxNormalization': ( 'preprocess.html#minmaxnormalization',
                                                                                      'fastspeech/preprocess.py'),
                                       'fastspeech.preprocess.MinMaxNormalization.__init__': ( 'preprocess.html#minmaxnormalization.__init__',
                                                                                               'fastspeech/preprocess.py'),
                                       'fastspeech.preprocess.MinMaxNormalization.denormalize': ( 'preprocess.html#minmaxnormalization.denormalize',
                                                                                                  'fastspeech/preprocess.py'),
                                       'fastspeech.preprocess.MinMaxNormalization.normalize': ( 'preprocess.html#minmaxnormalization.normalize',
                                                                                                'fastspeech/preprocess.py'),
                                       'fastspeech.preprocess.Vocab': ('preprocess.html#vocab', 'fastspeech/preprocess.py'),
                                       'fastspeech.preprocess.Vocab.__getitem__': ( 'preprocess.html#vocab.__getitem__',
                                                                                    'fastspeech/preprocess.py'),
                                       'fastspeech.preprocess.Vocab.__init__': ( 'preprocess.html#vocab.__init__',
                                                                                 'fastspeech/preprocess.py'),
                                       'fastspeech.preprocess.Vocab.__len__': ('preprocess.html#vocab.__len__', 'fastspeech/preprocess.py'),
                                       'fastspeech.preprocess.Vocab._load_vocab': ( 'preprocess.html#vocab._load_vocab',
                                                                                    'fastspeech/preprocess.py'),
                                       'fastspeech.preprocess.ZScoreNormalization': ( 'preprocess.html#zscorenormalization',
                                                                                      'fastspeech/preprocess.py'),
                                       'fastspeech.preprocess.ZScoreNormalization.__init__': ( 'preprocess.html#zscorenormalization.__init__',
                                                                                               'fastspeech/preprocess.py'),
                                       'fastspeech.preprocess.ZScoreNormalization.denormalize': ( 'preprocess.html#zscorenormalization.denormalize',
                                                                                                  'fastspeech/preprocess.py'),
                                       'fastspeech.preprocess.ZScoreNormalization.normalize': ( 'preprocess.html#zscorenormalization.normalize',
                                                                                                'fastspeech/preprocess.py'),
                                       'fastspeech.preprocess.argmax_all': ('preprocess.html#argmax_all', 'fastspeech/preprocess.py'),
                                       'fastspeech.preprocess.flatten_and_concat': ( 'preprocess.html#flatten_and_concat',
                                                                                     'fastspeech/preprocess.py'),
                                       'fastspeech.preprocess.map_tensors': ('preprocess.html#map_tensors', 'fastspeech/preprocess.py'),
                                       'fastspeech.preprocess.pad_duration': ('preprocess.html#pad_duration', 'fastspeech/preprocess.py'),
                                       'fastspeech.preprocess.pad_max_seq': ('preprocess.html#pad_max_seq', 'fastspeech/preprocess.py'),
                                       'fastspeech.preprocess.pad_mels': ('preprocess.html#pad_mels', 'fastspeech/preprocess.py'),
                                       'fastspeech.preprocess.pad_phones': ('preprocess.html#pad_phones', 'fastspeech/preprocess.py'),
                                       'fastspeech.preprocess.phones_list_to_num': ( 'preprocess.html#phones_list_to_num',
                                                                                     'fastspeech/preprocess.py'),
                                       'fastspeech.preprocess.round_and_align_durations': ( 'preprocess.html#round_and_align_durations',
                                                                                            'fastspeech/preprocess.py'),
                                       'fastspeech.preprocess.transform_inp': ('preprocess.html#transform_inp', 'fastspeech/preprocess.py'),
                                       'fastspeech.preprocess.trim_audio': ('preprocess.html#trim_audio', 'fastspeech/preprocess.py')},
            'fastspeech.training': { 'fastspeech.training.FastspeechLearner': ('training.html#fastspeechlearner', 'fastspeech/training.py'),
                                     'fastspeech.training.FastspeechLearner.__init__': ( 'training.html#fastspeechlearner.__init__',
                                                                                         'fastspeech/training.py'),
                                     'fastspeech.training.FastspeechLearner._update_bar_and_history': ( 'training.html#fastspeechlearner._update_bar_and_history',
                                                                                                        'fastspeech/training.py'),
                                     'fastspeech.training.FastspeechLearner.fit': ( 'training.html#fastspeechlearner.fit',
                                                                                    'fastspeech/training.py'),
                                     'fastspeech.training.FastspeechLearner.load_model_state_dict': ( 'training.html#fastspeechlearner.load_model_state_dict',
                                                                                                      'fastspeech/training.py'),
                                     'fastspeech.training.FastspeechLearner.one_step': ( 'training.html#fastspeechlearner.one_step',
                                                                                         'fastspeech/training.py'),
                                     'fastspeech.training.FastspeechLearner.save_model': ( 'training.html#fastspeechlearner.save_model',
                                                                                           'fastspeech/training.py'),
                                     'fastspeech.training.TransformerScheduler': ( 'training.html#transformerscheduler',
                                                                                   'fastspeech/training.py'),
                                     'fastspeech.training.TransformerScheduler.__init__': ( 'training.html#transformerscheduler.__init__',
                                                                                            'fastspeech/training.py'),
                                     'fastspeech.training.TransformerScheduler._get_lr_scale': ( 'training.html#transformerscheduler._get_lr_scale',
                                                                                                 'fastspeech/training.py'),
                                     'fastspeech.training.TransformerScheduler._update_learning_rate': ( 'training.html#transformerscheduler._update_learning_rate',
                                                                                                         'fastspeech/training.py'),
                                     'fastspeech.training.TransformerScheduler.step': ( 'training.html#transformerscheduler.step',
                                                                                        'fastspeech/training.py'),
                                     'fastspeech.training.count_parameters': ('training.html#count_parameters', 'fastspeech/training.py'),
                                     'fastspeech.training.load_checkpoint': ('training.html#load_checkpoint', 'fastspeech/training.py'),
                                     'fastspeech.training.mae_loss': ('training.html#mae_loss', 'fastspeech/training.py')},
            'fastspeech.visualize': { 'fastspeech.visualize.plot_loss': ('visualize.html#plot_loss', 'fastspeech/visualize.py'),
                                      'fastspeech.visualize.plot_phoneme_durations': ( 'visualize.html#plot_phoneme_durations',
                                                                                       'fastspeech/visualize.py'),
                                      'fastspeech.visualize.plot_wav': ('visualize.html#plot_wav', 'fastspeech/visualize.py'),
                                      'fastspeech.visualize.show_mel': ('visualize.html#show_mel', 'fastspeech/visualize.py'),
                                      'fastspeech.visualize.show_mels': ('visualize.html#show_mels', 'fastspeech/visualize.py')}}}
