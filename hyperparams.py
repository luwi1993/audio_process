class hyperparams:
    # main params
    model_name = "GAN"
    path = "/Users/luwi/Documents/Datasets/Emotional_Speech/LJSpeech-1.1/wavs/"
    dataloader_path = "files/dataloader_" + model_name + ".pth"

    # stft params
    sample_rate = 22050
    nfft = 2048
    hop_length = 512
    window_length = 2048

    # Eq settings
    eq_mode = "linear"

    # feature params
    silence_db = 30
    preemphasis = 0.97

    max_db = 100
    ref_db = 20

    n_features = 80
    temporal_rate = 32
    feature_mode = "mel"

    label_mode = "binary"
    one_hot = False
    binary_class = "sa"
    num_classes = 2

    # dataset params
    load_n = 10000
    batch_size = 64
    split = {"train": 0.6, "test": 0.2, "valid": 0.2}
    verbose = True  # TODO use this consequently

    # model params
    dropout = 0.05
    hidden_dim = 256

    # training params
    device = 'cpu'
    lr = 0.00005
    n_epochs = 1000
