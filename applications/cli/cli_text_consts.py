#
# Copyright (c) 2019 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

VERBOSE_RERUN_MSG = "Use -v or -vv option for more info."
SPINNER_COLOR = "green"


class VersionCmdTexts:
    HELP = "Displays the version of the installed nctl application."
    INITIAL_PLATFORM_VERSION = "Failed to acquire platform version."
    KUBECTL_INT_ERROR_MSG = "Falied to check platform version. This may occur for example due to invalid path to " \
                            "kubectl config, invalid k8s credentials or k8s cluster being unavailable. Check your " \
                            "KUBECONFIG environment variable and make sure that the k8s cluster is online."
    OTHER_ERROR_MSG = "Unexpected error occurred during platform version check."
    TABLE_APP_ROW_NAME = "nctl application"
    TABLE_PLATFORM_ROW_NAME = "nauta platform"
    TABLE_HEADERS = ["Component", "Version"]


class MountCmdTexts:
    HELP = "Displays a command that can be used to mount a client's folder on their local machine."
    MAIN_MSG = """
|=======================================================================================================|
|   <NAUTA_FOLDER>  |   Code Reference Path     |   User Access     |   Shared Access                   |
|-------------------------------------------------------------------------------------------------------|
|   input           |   /mnt/input/home         |   read/write      |   -                               |
|   output          |   /mnt/output/home        |   read/write      |   -                               |
|   input-shared    |   /mnt/input/root/public  |   read/write      |   read/write                      |
|   output-shared   |   /mnt/output/root/public |   read/write      |   read/write                      |
|   input-output-ro |                           |   read            |   read                            |
|=======================================================================================================|
|   Each experiment has a special folder that can be accessed                                           |
|   as /mnt/output/experiment from training script. This folder is shared by Samba                      |
|   as output/<EXPERIMENT_NAME>.                                                                        |
|=======================================================================================================|
|   <MOUNTPOINT>    |   folder/drive location on your local machine                                     |
|=======================================================================================================|
    """

    MOUNT_CMD = "Mount command for this operating system:\n{command}" 

    HELP_L = "Displays a list of nauta folders mounted on a local machine. If run using administrator credentials, displays " \
             "mounts of all users."
    GET_MOUNT_COMMAND_ERROR_MSG = "Error detected while gathering data needed for mounting Samba share."
    UNMOUNT_CMD = "Unmount previously mounted folder using the command:\n{command}"
    UNMOUNT_OPTIONS_MSG = "If unmounting issues occur (disconnected disk, etc.), try to use the -f (force) " \
                           "or -l (lazy) command to resolve. For more information about these options, refer to man umount."
    UNMOUNT_OPTIONS_OSX_MSG = "If unmounting issues occur (disconnected disk, etc.), try to use the -f (force) " \
                              "or -l (lazy) command to resolve. For more information about these options, refer to man umount."
    UNMOUNT_MSG_UNIX = """
Example usage:
    - Mounting a local folder (mylocalfolder) to the user's Nauta input folder:
        sudo mount.cifs -o username=JANEDOE,password=lqS9P5kQ0TFzMmscCY21ZklDDKZtdBeH,rw,uid=10001 //10.91.120.152/input mylocalfolder
    - Code reference path:
        data_dir=/mnt/input/home/<Uploaded-DataFolder>
    - Unmount the folder:
        umount mylocalfolder
    """
    UNMOUNT_MSG_WIN = """
Example usage:
    - Mounting a local folder (mylocalfolder) to the user's Nauta input folder:
        net use mylocalfolder \\10.91.120.152\\input /user:JANEDOE lqS9P5kQ0TFzMmscCY21ZklDDKZtdBeH
    - Code reference path:
        data_dir=/mnt/input/home/<Uploaded-DataFolder>
    - Unmount the folder:
        net use mylocalfolder /d
    """
    MOUNTS_LIST_COMMAND_ERROR_MSG = "Error detected while gathering list of mounted shares."
    ADMIN_CHECK_ERROR_MSG = "Problems detected while verifying current user privileges."


class CmdsCommonTexts:
    INVALID_REGEX_ERROR_MSG = "Regular expression provided for name filtering is invalid: {name}"
    OTHER_ERROR_MSG = "Failed to get experiments list."
    PROXY_CREATION_ERROR_MSG = "Error occurred during creation of a proxy for elasticsearch."
    LOGS_GET_OTHER_ERROR_MSG = "Failed to get {instance_type} logs."
    EXPERIMENT_NOT_EXISTS_ERROR_MSG = "{instance_type} with name {experiment_name} does not exist."
    LOCAL_PORT_OCCUPIED_ERROR_MSG = "Error occurred during creation of a proxy for elasticsearch. {exe.message}"
    PROXY_CLOSE_LOG_ERROR_MSG = "Error occurred during closing of a proxy for elasticsearch."
    PROXY_CLOSE_USER_ERROR_MSG = "Elasticsearch proxy has not been closed properly. Check if it still exists, if " \
                                 "yes - close it manually."
    NAME_M_BOTH_GIVEN_ERROR_MSG = "Both {instance_type} name and -m option cannot be given. Choose one."
    NAME_M_NONE_GIVEN_ERROR_MSG = "Error: {instance_type} name or -m option must be given. Pass one."
    LOGS_STORING_CONF = "Logs from the {instance_name} {instance_type} will be stored in " \
                        "the {filename} file. Should the app proceed?"
    LOGS_STORING_CONF_FILE_EXISTS = "Logs from the {instance_name} {instance_type} will be stored in the " \
                                    "{filename} file. The file with this name already exists. Should the app " \
                                    "proceed?"
    LOGS_STORING_ERROR = "Some problems occurred during storing a file with logs."
    LOGS_STORING_FINAL_MESSAGE = "Logs have been written to the file mentioned above."
    LOGS_STORING_CANCEL_MESSAGE = "Logs have not been written to the file mentioned above, cancelled by user." 
    MORE_EXP_LOGS_MESSAGE = "There is more than one log to be stored. Each log will be stored in a separate file."
    SAVING_LOGS_TO_FILE_PROGRESS_MSG = "Saving logs to a file..."


class VerifyCmdTexts:
    HELP = "Verifies if all required external components contain the proper installed versions."
    KUBECTL_NOT_INSTALLED_ERROR_MSG = "kubectl is not installed."
    KUBECTL_INVALID_VERSION_ERROR_MSG = "The installed version of kubectl ({installed_version}) is not " \
                                        "supported, supported version {supported_versions_sign} {expected_version}"
    GET_K8S_NAMESPACE_ERROR_MSG = "Failed to get current Kubernetes namespace."
    VERSION_CHECKING_MSG = "Checking version of {dependency_name}. Installed version: ({installed_version}). " \
                           "Supported version {supported_versions_sign} {expected_version}."
    DEPENDENCY_VERIFICATION_SUCCESS_MSG = "{dependency_name} verified successfully."
    INVALID_VERSION_WARNING_MSG = "Warning: the installed version of {dependency_name} ({installed_version}) is " \
                                  "not supported, supported version {supported_versions_sign} " \
                                  "{expected_version}"
    DEPENDENCY_NOT_INSTALLED_ERROR_MSG = "{dependency_name} is not installed. Check installation manual for more " \
                                         "information."
    DEPENDENCY_VERSION_CHECK_ERROR_MSG = "Failed to get {dependency_name} version."
    DEPENDENCY_VERIFICATION_OTHER_ERROR_MSG = "{dependency_name} - exception during verification."
    OS_SUPPORTED_MSG = "This OS is supported."
    CHECKING_CONNECTION_TO_CLUSTER_MSG = "Checking connection to the cluster..."
    CHECKING_OS_MSG = "Checking operating system..."
    VERIFYING_DEPENDENCY_MSG = "Verifying {dependency_name} ..."
    CHECKING_PORT_FORWARDING_FROM_CLUSTER_MSG = "Checking port forwarding from cluster..."
    WRONG_REQUIREMENTS_SETTINGS = "- {pack_name}"
    VERIFYING_RESOURCES_CORRECTNESS = "Verifying packs resources' correctness ..."
    INCORRECT_PACKS_EXIST = "The following packs have incorrect resources' settings. Use the 'config' command to " \
                            "align those settings with resources available on a cluster."


class ModelProcessListCmdTexts:
    HELP = "Displays a list of available processing templates."
    PROCESS_LIST_ERROR_MSG = "Error during getting list of processing workflows."


class UserCmdTexts:
    HELP = "Create, delete, or list users of the platform. Can only be run by a platform administrator."


class UserListCmdTexts:
    HELP = "List users."
    HELP_C = "If given - command displays c last rows."
    TABLE_HEADERS = ["Name", "Creation date", "Date of last submitted job", "Number of running jobs",
                     "Number of queued jobs"]
    OTHER_ERROR_MSG = "Failed to get users list."


class UserCreateCmdTexts:
    SHORT_HELP = "Create a new user on the platform. Can only be run by a platform administrator."
    HELP = """
   Create a new user on the platform. Can only be run by a platform administrator. 

    USERNAME - is a name of user which should be created.
    """
    HELP_L = "If given, content of the generated user's configuration file is displayed on the screen only."
    HELP_F = "Name of file where user's configuration will be stored. If not given, configuration is stored in the " \
             "config. file."
    ADD_USER_ERROR_MSG = "User {username} has not been created."
    REMOVE_USER_ERROR_MSG = "Additional error appeared when the system tried to remove artifacts of a non-created " \
                            "{username} user. Contact an administrator to completely remove those artifacts."
    F_L_OPTIONS_EXCLUSION_ERROR_MSG = "Both -fl/--filename and -lo/--list_only options cannot be given.  " \
                                      "Choose one."
    NAME_VALIDATION_ERROR_MSG = "Error detected while validating user name: {username}."
    USER_ALREADY_EXISTS_ERROR_MSG = "User {username} already exists."
    USER_BEING_REMOVED_ERROR_MSG = "User {username} is still being removed."
    USER_VERIFICATION_ERROR_MSG = "Problems detected while verifying user with user name: {username}."
    PASSWORD_GATHER_ERROR_MSG = "The app encountered problems while gathering user's password."
    CERT_GATHER_ERROR_MSG = "The app encountered problems while gathering server's certifcate authority."
    GIT_REPO_MANAGER_ERROR_MSG = "Error detected while adding the user to git repo manager."
    USER_ADD_ERROR_MSG = "Error detected while adding of a user."
    USER_CREATION_SUCCESS_MSG = "User {username} has been added successfully."
    USER_NOT_READY_ERROR_MSG = "User {username} is still not ready."
    CONFIG_CREATION_ERROR_MSG = "Problems during creation of the kubeconfig with user's configuration."
    LIST_ONLY_HEADER = "Use the following kubectl config to connect to this user.\n" \
                       "----------------------------------------------------------------"
    CONFIG_SAVE_SUCCESS_MSG = "Configuration has been saved to the {filename} file."
    CONFIG_SAVE_FAIL_MSG = "File with configuration was not saved."
    CONFIG_SAVE_FAIL_INSTRUCTIONS_MSG = "Content of the generated configuration file is as follows. Copy it " \
                                        "to a file manually."
    CREATING_USER_PROGRESS_MSG = "Creating user {username}..."


class UserDeleteCmdTexts:
    SHORT_HELP = "Delete a user from the platform. Can be only run by a platform administrator."
    HELP = """
    Delete a user from the platform. Can be only run by a platform administrator.

    USERNAME - is a name of user which should be deleted.
    """
    HELP_PR = "If this option is added, the command removes all of client's artifacts."
    USER_NOT_EXISTS_ERROR_MSG = "User {username} does not exist."
    USER_BEING_REMOVED_ERROR_MSG = "User is still being removed."
    USER_PRESENCE_VERIFICATION_ERROR_MSG = "Problems during verifying users presence."
    DELETE_CONFIRM_MSG = "User {username} is about to be deleted. Do you want to continue?"
    DELETE_ABORT_MSG = "Operation of deleting of a user was aborted."
    PURGE_ERROR_MSG = "Some artifacts belonging to a user were not removed."
    DELETE_IN_PROGRESS_MSG = "User is still being deleted. Wait a few minutes, then check the user's status."
    DELETE_SUCCESS_MSG = "User {username} has been deleted."
    PROXY_ERROR_LOG_MSG = "Error occurred during closing of a proxy for elasticsearch."
    PROXY_ERROR_USER_MSG = "Elasticsearch proxy has not been closed correctly. Check if it still exists. If " \
                           "yes, close it manually."
    OTHER_ERROR_LOG_MSG = "Error occurred during deleting a user of a user."
    OTHER_ERROR_USER_MSG = "User has not been deleted due to technical reasons."
    DELETION_CHECK_PRESENCE = "Checking presence of a user that is going to be deleted..."
    DELETION_START_DELETING = "Deleting of a user is starting now..."
    DELETION_START_PURGING = "Purging of a user is starting now..."
    DELETION_VERIFICATION_OF_DELETING = "Verifying, whether a user has been deleted correctly..."
    DELETION_DELETING_NAMESPACE = "- Deleting user's namespace."
    DELETION_DELETING_USERS_OBJECTS = "- Deleting user's objects."
    DELETION_DELETING_USERS_EXPERIMENTS = "- Deleting user experiments' logs."
    DELETION_DELETING_USERS_REPOSITORY = "- Deleting user's repository."


class UserUpgradeCmdTexts:
    SHORT_HELP = "Upgrade users on the platform. Can only be run by a platform administrator."
    UPGRADE_IN_PROGRESS = "Users upgrade in progress..."
    UPGRADE_SUCCEEDED = "Users upgrade succeeded."
    UPGRADE_FAILED = "Users upgrade failed."


class LaunchCmdTexts:
    HELP = "Launch the web user-interface or TensorBoard. Runs as a process in the system console until the " \
           "user stops the process. To run in the background, add '&' at the end of the line."
    HELP_P = "Port on which service will be exposed locally."
    HELP_N = "Run the command without a web browser starting. Only proxy tunnel is created"
    WEBUI_HELP = "Subcommand for launching webUI with credentials."
    APP_PROXY_EXISTS_ERROR_MSG = "K8s proxy has not been closed correctly. Check if it still exists. If yes, " \
                                 "close it manually."
    APP_PROXY_OTHER_ERROR_MSG = "Other exception during launching web application."
    SHORT_TB_HELP = "Subcommand for launching tensorboard with credentials."
    TB_HELP = """
    Subcommand for launching TensorBoard with credentials.

    EXPERIMENT_NAME - is a name of experiment for which TensorBoard instance should be launched.
    """
    TB_HELP_TSCP = "Local port on which TensorBoard service client will be started."
    TB_INVALID_RUNS_MSG = "There is no data for the following experiments : {invalid_runs}\n" \
                          "TensorBoard will present information from the rest of given experiments."
    TB_CREATE_ERROR_MSG = "Failed to create tensorboard!"
    TB_WAITING_MSG = "Wait for TensorBoard to run..."
    TB_WAITING_FOR_TB_MSG = "TensorBoard instance: {tb_id} still in {tb_status_value} status, waiting for " \
                            "RUNNING..."
    TB_TIMEOUT_ERROR_MSG = "TensorBoard failed to run: timeout."


class PredictCmdTexts:
    HELP = "Start, stop, and manage prediction jobs and instances."


class PredictListCmdTexts:
    HELP = "Show prediction instances."
    HELP_A = "Show all prediction instances, regardless of the owner."
    HELP_N = "A regular expression to narrow down the list to prediction instances that match this expression."
    HELP_S = "List prediction instances with matching status."
    HELP_U = "List uninitialized prediction instances. For example, prediction instances" \
             " without resources submitted for creation."
    HELP_C = "If given, this command displays c last rows."
    HELP_B = "Use to print short version of the experiment result table."


class PredictLaunchCmdTexts:
    HELP = "Starts a new prediction instance that can be used for performing prediction, classification and " \
           "regression tasks on trained model."
    HELP_N = "The name of this prediction instance."
    HELP_M = "Path to saved model that will be used for inference. Model must be located on one of the input or " \
             "output system shares (for example: /mnt/input/saved_model)."
    HELP_R = "Path to file with experiment's pip requirements." \
             " Dependencies listed in this file will be automatically installed using pip."
    INSTANCE_START_ERROR_MSG = "Failed to create prediction instance."
    INSTANCE_INFO_MSG = "\nPrediction instance URL (append method verb manually. For example, :predict):\n" \
                        "{inference_instance_url}\n\nAuthorize with following header:\n{authorization_header}"
    INSTANCE_URL_ERROR_MSG = "Failed to obtain prediction instance URL."
    TABLE_HEADERS = ["Prediction instance", "Model Location", "Status"]
    HELP_LOCAL_MODEL_LOCATION = "Local path to saved model that will be used for inference. Model content will be " \
                                "copied into an image."
    MODEL_DIR_NOT_FOUND_ERROR_MSG = "Cannot find: {local_model_location}. local_model_location must be a path to " \
                                    "existing directory."
    MISSING_MODEL_LOCATION_ERROR_MSG = "Missing model location parameter - " \
                                       "'model location' or 'local model location' required."
    HELP_MODEL_NAME = "Name of a model passed as a servable name. By default, it is the name of directory in model's " \
                      "location."
    HELP_P = " Additional pack parameter in format: 'key value' or 'key.subkey.subkey2 value'. For lists use: " \
             "'key \"['val1', 'val2']\"' For maps use: 'key \"{'a': 'b'}\"' "
    HELP_RT = "Determine runtime for prediction. Supported runtimes are 'TensorFlow serving' and 'OpenVINO Model " \
              "Server'. Default option is 'tfserving'."

    PREDICTION_INSTANCE_NOT_READY = "Prediction instance is not ready. Wait a few minutes, then check its readiness again."

class PredictStreamCmdTexts:
    HELP = "Perform stream prediction task on deployed prediction instance."
    HELP_N = "Name of prediction session."
    HELP_D = "Path to JSON data file that will be streamed to prediction instance. Data must be formatted so " \
             "that it is compatible with the SignatureDef specified within the model deployed in selected " \
             "prediction instance."
    HELP_M = "Method verb that will be used when performing inference. Predict verb is used by default."
    INSTANCE_NOT_EXISTS_ERROR_MSG = "Prediction instance {name} does not exist."
    INSTANCE_NOT_RUNNING_ERROR_MSG = "Prediction instance {name} is not in {running_code} state."
    INSTANCE_GET_FAIL_ERROR_MSG = "Failed to get prediction instance {name} URL."
    JSON_LOAD_ERROR_MSG = "Failed to load {data} data file. Make sure that provided file exists and is in a " \
                          "valid JSON format."
    INFERENCE_OTHER_ERROR_MSG = "Failed to perform inference. Reason: {exception}"
    INFERENCE_ERROR_RESPONSE_MSG = "\n Response: {response_text}"
    WAITING_FOR_RESPONSE_MSG = "Waiting for prediction instance response..."


class PredictCancelCmdTexts:
    SHORT_HELP = "Cancels prediction instance/s chosen based on criteria given as a parameter."
    HELP = """
    Cancels prediction instance/s chosen based on criteria given as a parameter.

    name - is a name of prediction instance which should be cancelled, the name argument value can be empty when the 'match' option is used.
    """
    HELP_P = "If given, then all prediction instances-related information, completed and currently " \
             "running, is removed from the system."
    HELP_M = "If given, the command searches for prediction instances matching the value of this option."
    EXPERIMENT_NAME = "prediction instance."
    EXPERIMENT_NAME_PLURAL = "prediction instances."


class PredictBatchCmdTexts:
    HELP = "Uses specified dataset to perform inference. Results are stored in the output file."
    HELP_DATA = "Location of a folder with data that will be used to perform the batch inference. Value should " \
                "point out the location from one of the system's shares."
    HELP_MODEL_LOCATION = "Path to saved model that will be used for inference. Model must be located on one of the " \
                          "input or output system shares. For example: /mnt/input/home/saved_model (user only access path)." \
                          "or /mnt/input/root/public/saved_model (shared access path)." 
    HELP_LOCAL_MODEL_LOCATION = "Local path to saved model that will be used for inference. Model content will be " \
                                "copied into an image."
    HELP_MODEL_NAME = "Name of a model passed as a servable name. By default it is the name of directory in model's " \
                      "location."
    HELP_NAME = "Name of a predict session."
    HELP_OUTPUT = "Location of a folder where outputs from inferences will be stored. Value should point out the " \
                  "location from one of the system's shares."
    HELP_REQUIREMENTS = "Path to file with experiment's pip requirements." \
                        " Dependencies listed in this file will be automatically installed using pip."
    OTHER_INSTANCE_CREATION_ERROR_MSG = "Failed to create batch prediction instance."
    TABLE_NAME_HEADER = "Prediction instance."
    TABLE_MODEL_LOCATION_HEADER = "Model location."
    TABLE_STATUS_HEADER = "Status."
    TABLE_HEADERS = ["Prediction instance", "Model location", "Status"]
    MODEL_DIR_NOT_FOUND_ERROR_MSG = "Cannot find: {local_model_location}. local_model_location must be a path to the " \
                                    "existing directory."
    MISSING_MODEL_LOCATION_ERROR_MSG = "Missing model location parameter - " \
                                       "'model location' or 'local model location' required."
    HELP_TF_RECORD = "If given, batch prediction accepts files in TFRecord formats. Otherwise, files should be " \
                     "delivered in protobuf format."
    HELP_P = " Additional pack parameter in format: 'key value' or 'key.subkey.subkey2 value'. For lists use: " \
             "'key \"['val1', 'val2']\"' For maps use: 'key \"{'a': 'b'}\"' "
    HELP_RT = "Determine runtime for prediction. Supported runtimes are 'TensorFlow serving' and 'OpenVINO Model " \
              "Server'. Default option is 'tfserving'."


class ExperimentCmdTexts:
    SHORT_HELP = "Start, stop, or manage training jobs."
    HELP = "Starting, stopping, and managing training jobs COMMAND."


class ExperimentListCmdTexts:
    SHORT_HELP = "List experiments."
    HELP_A = "Displays all experiments."
    HELP_N = "Displays a list of experiments that match this expression."
    HELP_S = "Displays experiments with matching status."
    HELP_U = "Displays a list of uninitialized experiments waiting for specified resources."
    HELP_C = "Displays the specified number of the most recent experiments."
    HELP_B = "Print short version of result table. Only 'name', 'submission date', 'owner' and 'state' columns will" \
             " be print."


class ExperimentTemplateListCmdTexts:
    SHORT_HELP = "Show logs for a given experiment."
    HELP = "Displays a list of available templates used to submit training jobs."
    LACK_OF_PACKS_ERROR_MSG = "Lack of installed packs."


class ExperimentLogsCmdTexts:
    SHORT_HELP = "Displays experiment logs."
    HELP = """
    Displays experiment logs.

    experiment_name - name of the experiment. The experiment_name argument value can be empty when 'match' 
    option is used.
    """
    HELP_S = "Displays all minimal and greater severity events."
    HELP_SD = "Retrieve all logs produced on and after this date (use ISO 8601 date format)."
    HELP_ED = "Retrieve all logs produced on and before this date (use ISO 8601 date format)."
    HELP_I = "Comma separated list of pod IDs. If provided, only logs from these pods will be returned."
    HELP_P = "Get logs only for pods with given status."
    HELP_M = "Searches for logs from experiments matching the value of this option. Cannot be used with the " \
             "experiment_name argument. "
    HELP_O = "Stores file-named experiment logs."
    HELP_F = "Specifies if logs should be streamed. Streams only logs from a single experiment."
    HELP_PAGER = "Display logs in interactive pager."


class PredictLogsCmdTexts:
    SHORT_HELP = "Show logs for a given prediction instance."
    HELP = """
    Show logs for a given prediction instance.

    name - is a name of a prediction instance whose logs should be displayed. The name argument 
    value can be empty when the 'match' option is used.
    """
    HELP_S = "Show all events with this specified minimal and greater severity."
    HELP_SD = "Retrieves logs produced on or after this date (ISO 8601 date format)."
    HELP_ED = "Retrieves logs produced on or before this date ( ISO 8601 date format)."
    HELP_I = "Lists comma-separated pod ID logs only."
    HELP_P = "Retrieves pod status logs only."
    HELP_M = "If given, command searches for logs from prediction instances matching the value of this option. " \
             "This option cannot be used along with the NAME argument."
    HELP_O = "If given - logs are stored in a file with a name derived from a name of a prediction instance."
    HELP_F = "Specify if logs should be streamed. Only logs from a single prediction instance can be streamed."
    HELP_PAGER = "Display logs in interactive pager."


class PredictViewCmdTexts:
    SHORT_HELP = "Displays prediction instance's details."
    HELP = """
    Displays prediction instance’s details.

    PREDICTION_INSTANCE_NAME - Prediction instance’s name.
    """
    CONTAINER_DETAILS_MSG = "\n- Name: {name}\n- Status: {status}\n- Volumes:\n  {volumes}\n- Resources:  {resources}"
    NOT_FOUND_ERROR_MSG = "Prediction instance \"{experiment_name}\" not found."
    PODS_PARTICIPATING_LIST_HEADER = "\nPods participating in the execution:\n"
    PODS_TABLE_HEADERS = ["Name", "Uid", "Pod Conditions", "Container Details"]
    VIEW_OTHER_ERROR_MSG = "Failed to get details of prediction instance {name}."
    CONTAINER_NOT_CREATED_MSG = "Not created"
    CONTAINER_RUNNING_MSG = "Running, started at: "
    CONTAINER_TERMINATED_MSG = "Terminated, "
    CONTAINER_WAITING_MSG = "Waiting, "
    CONTAINER_REQUESTS_LIST_HEADER = "- Requests:\n{}"
    CONTAINER_LIMITS_LIST_HEADER = "- Limits:\n{}"
    RESOURCES_SUM_LIST_HEADER = "\nResources used by pods:\n"
    RESOURCES_SUM_PARSING_ERROR_MSG = "There was an error when trying to parse pods resources. Error msg: {error_msg}"
    RESOURCES_SUM_TABLE_HEADERS = ["Resource type", "Total usage"]
    RESOURCES_SUM_TABLE_ROWS_HEADERS = ["CPU requests:", "Memory requests:", "CPU limits:", "Memory limits:"]
    INSUFFICIENT_RESOURCES_MESSAGE = "Prediction instance is in QUEUED state due to insufficient {resources}."
    TOP_CPU_CONSUMERS = "Top CPU consumers: {consumers}"
    TOP_MEMORY_CONSUMERS = "Top memory consumers: {consumers}"
    PROBLEMS_WHILE_GATHERING_USAGE_DATA = "Reasons of QUEUED state and top consumers cannot be displayed due to " \
                                          "errors."
    PROBLEMS_WHILE_GATHERING_USAGE_DATA_LOGS = "Error when gathering consumers data."
    HELP_U = "Name of a user to who belongs viewed prediction instance." \
             " If not given - only prediction instances of a current " \
             "user are taken into account."
    REASON = "\n  Reason: "


class ExperimentSubmitCmdTexts:
    SHORT_HELP = "Used to submit training scripts."
    HELP = """
    Used to submit training scripts.

    SCRIPT-LOCATION - Required argument that shows the location of the script used for training purposes.

    script-parameters - Used to pass parameters directly to the script. When used, parameters should be added at the 
    end of command after '--' a string.
    """
    HELP_N = "Name for this experiment."

    HELP_SFL = "Location and name folder with additional files used by a script, for example: other .py files, data, etc. If not given, then its contents will not be copied into a Docker image created by the nctl submit command.  nctl copies all content, preserving its structure including subfolder(s)."
    HELP_T = "Name of a template used by nctl to create a description of a job to be submitted. If not given, a default template for single node TensorFlow training is used (tf-training). A list of available templates can be obtained by issuing the nctl experiment template_list command."     
    HELP_P = " Additional pack parameter in format: 'key value' or 'key.subkey.subkey2 value'. For lists use: " \
             "'key \"['val1', 'val2']\"' For maps use: 'key \"{'a': 'b'}\"' "         
    HELP_PR = "Values (set or range) of a single parameter."
    HELP_PS = "Values for one or several parameters."
    HELP_E = "Environment variables passed to training. You can pass as many environmental variables as desired. Each variable in such cases should be passed as a separate -e parameter."
    HELP_R = "Path to file containing an experiment's pip requirements. Dependencies listed in this file are automatically installed using pip."
    SCRIPT_NOT_FOUND_ERROR_MSG = "Cannot find: {script_location}. Make sure that provided path is correct."
    DEFAULT_SCRIPT_NOT_FOUND_ERROR_MSG = "Cannot find script: {default_script_name} in directory: " \
                                         "{script_directory}. If path to directory was passed as submit command " \
                                         "argument, then {default_script_name} file has to exist in that directory."
    SCRIPT_DIR_NOT_FOUND_ERROR_MSG = "Cannot find: {script_folder_location}. script_folder_location must be a path " \
                                     "to existing directory. "
    DUPLICATED_PACK_PARAM = "Pack parameter was provided more than once. Set the '{pack_param}' parameter correctly."
    SUBMIT_START_LOG_MSG = "Submit - start"
    SUBMIT_START_USER_MSG = "Submitting experiments."
    SUBMIT_ERROR_MSG = "Problems during submitting experiment: {exception_message}"
    SUBMIT_OTHER_ERROR_MSG = "Other problems during submitting experiment."
    FAILED_RUNS_LOG_MSG = "There are failed runs"


class ExperimentInteractCmdTexts:
    SHORT_HELP = "Launches local browser with Jupyter Notebook."
    HELP = "Launches local browser with Jupyter Notebook. If the script name argument is given, then script is put " \
           "into the opened notebook."
    HELP_N = "The name of this Jupyter Notebook session."
    HELP_F = "File with a notebook or a python script that should be opened in Jupyter Notebook."
    HELP_PN = "Port on which service will be exposed locally."
    HELP_P = " Additional pack parameter in format: 'key value' or 'key.subkey.subkey2 value'. For lists use: " \
             "'key \"['val1', 'val2']\"' For maps use: 'key \"{'a': 'b'}\"' "
    HELP_NO_LAUNCH = "Run command without a web browser starting. Only a proxy tunnel is created"
    EXPERIMENT_GET_ERROR_MSG = "Problems during loading a list of experiments."
    NAME_ALREADY_USED = "The chosen name ({name}) is already used by an experiment other than Jupyter Notebook. " \
                        "Choose another one."
    CONFIRM_EXPERIMENT_CREATION = "Experiment with a given name does not exist. Should the app continue and create a " \
                                  "new one? "
    SUBMITTING_EXPERIMENT_USER_MSG = "Submitting interactive experiment."
    SUBMIT_ERROR_MSG = "Error occurred during starting Jupyter Notebook session: {exception_message}"
    SUBMIT_OTHER_ERROR_MSG = "Other error during starting Jupyter Notebook session."
    SESSION_EXISTS_MSG = "Jupyter Notebook's session exists. nctl connects to this session ..."
    FILENAME_BUT_SESSION_EXISTS = "Jupyter Notebook's session exists - \"interact\" however, the command cannot be used with " \
                                  "\"-f/--filename\" option in this case."
    NOTEBOOK_STATE_CHECK_ERROR_MSG = "Error occurred during checking state of Jupyter Notebook."
    ATTACHING_SCRIPT_NOT_SUPPORTED_MSG = "Attaching script to existing Jupyter Notebook's session is not supported. " \
                                         "Create a new Jupyter Notebook's session to attach script."
    NOTEBOOK_NOT_READY_ERROR_MSG = "Jupyter Notebook is still not ready. Try to connect to the notebook by running " \
                                   "interact command another time, passing a name of a current Jupyter Notebook " \
                                   "session."
    PROXY_CLOSING_ERROR_MSG = "K8s proxy has not been closed correctly. Check if it still exists. If yes, close " \
                              "it manually."
    SESSION_LAUNCH_OTHER_ERROR_MSG = "Other exception during launching interact session."
    EXP_WITH_THE_SAME_NAME_MUST_BE_PURGED = "Notebook with the same name exists but is in state other than RUNNING. " \
                                            "If you want to start another notebook using the same name, " \
                                            "purge the previous one."
    HELP_E = "Environment variables passed to Jupyter instance. User can pass as many environmental variables as " \
             " desired. Each variable should be passed as a separate -e paramater."
    HELP_T = "Name of a Jupyter Notebook template used to create a deployment. " \
             "Supported template for interact command is: jupyter"
    TOO_MANY_JUPYTERS = "You have {jupyter_number} opened Jupyter notebooks. Do you still want to open another one?"
    INTERACT_ABORT_MSG = "Operation of starting a new Jupyter Notebook was aborted."


class ExperimentCancelCmdTexts:
    SHORT_HELP = "Cancels experiment/s or deletes selected pods."
    HELP = """
    Cancels experiment/s or deletes selected pods.

    name - is a name of experiment which should be cancelled, name argument value can be empty when 'match'
    option is used.
    """
    HELP_P = "If given, then all information concerning all experiments, completed and currently running, is removed " \
             "from the system."
    HELP_M = "If given, command searches for experiments matching the value of this option. This option cannot be " \
             "used along with the name argument."
    HELP_I = "Comma-separated pods IDs. If given, then matches pods by their IDs and deletes them."
    HELP_S = "One of: {available_statuses} - searches pods by their status and deletes them."
    NAME_M_BOTH_GIVEN_ERROR_MSG = "Both name and -m option cannot be given. Choose one of them."
    NAME_M_NONE_GIVEN_ERROR_MSG = "Error: Name or -m option must be given. Pass one of them."
    LIST_RUNS_ERROR_MSG = "Problems during loading a list of {experiment_name_plural}."
    LACK_OF_EXPERIMENTS_ERROR_MSG = "Lack of {experiment_name_plural} fulfilling given criteria. Name or match " \
                                    "string parameters do not match any existing {experiment_name} in an appropriate " \
                                    "state for the command. Run 'nctl exp list' to display the names and " \
                                    "states of existing {experiment_name_plural}."
    LACK_OF_EXP_TO_BE_CANCELLED_ERROR_MSG = "Lack of {experiment_name_plural} that can be cancelled. However, there " \
                                            "are {experiment_name_plural} that match given criteria and can be " \
                                            "purged. To remove them, rerun the cancel command " \
                                            "with the -p option."
    EXP_THAT_CAN_BE_PURGED_EXIST = "Lack of {experiment_name_plural} that can be cancelled, there are " \
                                   "{experiment_name_plural} that can be purged. To remove them, rerun" \
                                   " the cancel command with the -p option."
    CANCEL_OPERATION = {
        "cancelled": "cancelled",
        "cancellation": "cancellation"
    }
    DELETE_OPERATION = {
        "deleted": "deleted",
        "deletion": "deletion"
    }
    EXPERIMENTS_ALREADY_CANCELLED_ERROR_MSG = "{experiment_name_plural} fulfilling given criteria have been " \
                                              "{operation_word} already."
    ALREADY_CANCELLED_LIST_HEADER = "The following {experiment_name_plural} have been {operation_word} already or " \
                                    "cannot be {operation_word} due to their current state:"
    CAN_BE_CANCELLED_LIST_HEADER = "The following {experiment_name_plural} can still be {operation_word}:"
    WILL_BE_CANCELLED_LIST_HEADER = "The following {experiment_name_plural} will be {operation_word}:"
    WILL_BE_PURGED_LIST_HEADER = "The following {experiment_name_plural} will be {operation_word}:"
    CONFIRM_CANCEL_MSG = "Do you want to continue with {operation_word} of those {experiment_name_plural}?"
    CANCELLATION_ABORTED_MSG = "Operation of {operation_word} of {experiment_name_plural} was aborted."
    OTHER_CANCELLING_ERROR_MSG = "Error occurred during cancelling an experiment."
    PROXY_CLOSING_ERROR_LOG_MSG = "Error occurred during closing of a proxy for elasticsearch."
    PROXY_CLOSING_ERROR_USER_MSG = "Elasticsearch proxy has not been closed correctly. Check if it still exists. " \
                                   "If yes, close it manually."
    PORT_OCCUPIED_ERROR_LOG_MSG = "Error occurred during creation of proxy. Port is occupied."
    PORT_OCCUPIED_ERROR_USER_MSG = "Error occurred during creation of a proxy for elasticsearch. {exception_message}"
    PROXY_OPEN_ERROR_MSG = "Error occurred during the creation of a proxy for elasticsearch."
    SUCCESSFULLY_CANCELLED_LIST_HEADER = "The following {experiment_name_plural} were {operation_word} successfully:"
    FAILED_TO_CANCEL_LIST_HEADER = "The following {experiment_name_plural} were not {operation_word} correctly:"
    GET_EXPERIMENT_ERROR_MSG = "Error occurred during loading experiment's data."
    PURGING_START_MSG = "Purging {run_name} experiment ..."
    INCOMPLETE_PURGE_ERROR_MSG = "Not all {experiment_name}'s components were removed correctly." \
                                  "Check to determine if any other artifacts remain."
    CANCELING_RUNS_START_MSG = "Cancelling {run_name} {experiment_name} ..."
    DELETING_RELATED_OBJECTS_MSG = "Deleting objects related to {run_name} {experiment_name} ..."
    CANCEL_SETTING_STATUS_MSG = "Setting {run_name} status to CANCELLED ..."
    INCOMPLETE_CANCEL_ERROR_MSG = "Not all components of {run_name} {experiment_name} were deleted ...\nExperiment " \
                                  "remains in its previous state."
    BAD_POD_STATUS_PASSED = "Wrong status: {status_passed} , available: {available_statuses}"
    LACK_OF_PODS_ERROR_MSG = "Lack of pods fulfilling given criteria. Pod ID or pod status parameters do not match " \
                             "any existing pod."
    GIT_REPO_MANAGER_ERROR_MSG = "Failed to delete experiment from Git Repo Manager."
    CANCELING_PODS_MSG = "Deleting the pod: {pod_name} ..."
    OTHER_POD_CANCELLING_ERROR_MSG = "Error occurred during deletion of the pod."
    UNINITIALIZED_EXPERIMENT_CANCEL_MSG = "Experiment {experiment_name} has no resources submitted for creation."
    PURGING_PROGRESS_MSG = 'Purging experiment {run_name}...'
    PURGING_LOGS_PROGRESS_MSG = 'Purging experiment {run_name} logs...'


class ExperimentViewCmdTexts:
    SHORT_HELP = "Displays details given experiment/s name."
    HELP = """
    Displays details given experiment/s name.

    EXPERIMENT_NAME - Experiment’s name.
    """

    HELP_T = "If given, then exposes a TensorBoard's instance with experiment's data."

    CONTAINER_DETAILS_MSG = "\n- Name: {name}\n- Status: {status}\n- Volumes:\n  {volumes}\n- Resources:  {resources}"
    NOT_FOUND_ERROR_MSG = "Experiment \"{experiment_name}\" not found."
    PODS_PARTICIPATING_LIST_HEADER = "\nPods participating in the execution:\n"
    PODS_TABLE_HEADERS = ["Name", "Uid", "Pod Conditions", "Container Details"]
    VIEW_OTHER_ERROR_MSG = "Failed to get details of experiment {name}."
    CONTAINER_NOT_CREATED_MSG = "Not created"
    CONTAINER_RUNNING_MSG = "Running, started at: "
    CONTAINER_TERMINATED_MSG = "Terminated, "
    CONTAINER_WAITING_MSG = "Waiting, "
    CONTAINER_REQUESTS_LIST_HEADER = "- Requests:\n{}"
    CONTAINER_LIMITS_LIST_HEADER = "- Limits:\n{}"
    RESOURCES_SUM_LIST_HEADER = "\nResources used by pods:\n"
    RESOURCES_SUM_PARSING_ERROR_MSG = "Error occurred when trying to parse a pod's resources. Error msg: {error_msg}"
    RESOURCES_SUM_TABLE_HEADERS = ["Resource type", "Total usage"]
    RESOURCES_SUM_TABLE_ROWS_HEADERS = ["CPU requests:", "Memory requests:", "CPU limits:", "Memory limits:"]
    INSUFFICIENT_RESOURCES_MESSAGE = "Experiment is in QUEUED state due to insufficient {resources}."
    TOP_CPU_CONSUMERS = "Top CPU consumers: {consumers}"
    TOP_MEMORY_CONSUMERS = "Top memory consumers: {consumers}"
    PROBLEMS_WHILE_GATHERING_USAGE_DATA = "Reasons of QUEUED state and top consumers cannot be displayed due to " \
                                          "errors."
    PROBLEMS_WHILE_GATHERING_USAGE_DATA_LOGS = "Error occurred when gathering consumer's data."
    HELP_U = "Name of a user to who belongs viewed experiment. If not given, only experiments of a current " \
             "user are considered."
    REASON = "\n  Reason: "


class ExperimentCommonTexts:
    CONFIRM_EXP_DIR_DELETION_MSG = "Experiment data directory: {run_environment_path} already exists. It will be " \
                                   "deleted to proceed with experiment submission. Do you want to continue?"
    UNABLE_TO_CONTINUE_EXP_SUBMISSION_ERROR_MSG = "Cannot continue experiment submission. Delete the experiment's " \
                                                  "data directory {run_environment_path} manually or use a different " \
                                                  "name for the experiment."
    CREATE_ENV_MSG_PREFIX = "Experiment's environment has not been created. Reason - {reason}"
    DIR_CANT_BE_COPIED_ERROR_TEXT = "Additional folder cannot be copied into experiment's folder."
    EXP_DIR_CANT_BE_CREATED = "Folder with experiments' data cannot be created."
    TRAINING_SCRIPT_CANT_BE_CREATED = "Training script cannot be created."
    GET_NAMESPACE_ERROR_MSG = "Failed to get current Kubernetes namespace."
    SUBMIT_PREPARATION_ERROR_MSG = "Problem occurred during preparation of experiments' data."
    LOCAL_DOCKER_TUNNEL_ERROR_MSG = "Error occurred during creation of a local docker-host tunnel."
    ENV_CREATION_ERROR_MSG = "Problems during creation of environments."
    CONFIRM_SUBMIT_MSG = "Confirm that the following experiments should be submitted."
    CONFIRM_SUBMIT_QUESTION_MSG = "Do you want to continue?"
    SUBMISSION_FAIL_ERROR_MSG = "Your Experiment submission failed. Use the verbose option to get more " \
                                "detailed information about failure's cause."
    PROXY_CLOSE_ERROR_MSG = "Docker proxy has not been closed correctly. Check if it still exists. If yes, close " \
                            "it manually."
    PROXY_OPEN_ERROR_MSG = "Error occurred during opening of a proxy for a docker registry."
    SUBMIT_OTHER_ERROR_MSG = "Other error during submitting experiments."
    DOCKER_TUNNEL_CLOSE_ERROR_MSG = "Local Docker-host tunnel has not been closed correctly. Check if it still " \
                                    "exists. If yes, close it manually."
    EXP_TEMPLATES_NOT_GENERATED_ERROR_MSG = "Experiment templates have not generated. Reason - {reason}"
    JOB_NOT_DEPLOYED_ERROR_MSG = "Job has not deployed. "
    INCORRECT_PARAM_FORMAT_ERROR_MSG = "Parameter {param_name} has incorrect format."
    PARAM_AMBIGUOUSLY_DEFINED = "Parameter {param_name} ambiguously defined."
    PARAM_SET_INCORRECT_FORMAT_ERROR_MSG = "One of -ps options has an incorrect format."
    INVALID_PACK_PARAM_FORMAT_ERROR_MSG = "Invalid pack params format for param: {key}. Key cannot contain '='. " \
                                          "Specify pack params in format 'key value' not as 'key=value'."
    EXPERIMENT_NAME_TOO_LONG_ERROR_MSG = "Name given by a user cannot be longer than 30 characters."
    ERROR_DURING_PATCHING_RUN = "Error occurred during patching a run occurred {}."
    PROBLEMS_DURING_GETTING_DRAFT_LOGS = "Error occurred during getting draft logs: {exception}"
    THE_SAME_EXP_IS_SUBMITTED = "There is another experiment with the same name submitted. Resubmit with a new name" \
                                "or choose to delete the existing experiment and submit the same name again."
    PREPARING_RESOURCE_DEFINITIONS_MSG = "Preparing resources' definitions..."
    CLUSTER_CONNECTION_MSG = "Connecting to the cluster..."
    CREATING_ENVIRONMENT_MSG = "Creating {run_name} environment..."
    CREATING_RESOURCES_MSG = "Creating {run_name} resources..."
    CLUSTER_CONNECTION_CLOSING_MSG = "Closing tunnel to the cluster..."
    INCORRECT_TEMPLATE_NAME = "Incorrect template name."
    INCORRECT_ENV_PARAMETER = "-e/--env option must be in <KEY>=<VALUE> format."
    INCORRECT_PACK_DEFINITION = "Definition of the {pack_name} pack is incorrect."
    ERROR_WHILE_REMOVING_EXPERIMENT = "Error occurred during removal of unsubmitted experiment."
    ERROR_WHILE_REMOVING_RUNS = "Error occurred during removal of unsubmitted runs."
    CTRL_C_PURGING_PROGRESS_MSG = "System removes already submitted experiments as a result of pressing Ctrl-C."


class DraftCmdTexts:
    DOCKER_IMAGE_NOT_BUILT = "Docker image has not been built."
    DOCKER_IMAGE_NOT_SENT = "Docker image has not been sent to the cluster."
    APP_NOT_RELEASED = "Application has not been released."
    DEPLOYMENT_NOT_CREATED = "Deployment has not been created."
    PACK_NOT_EXISTS = "Chosen pack does not exist."


class PacksTfTrainingTexts:
    CONFIG_NOT_UPDATED = "Configuration has not been updated."
    CANT_PARSE_VALUE = "Cannot parse value: \"{value}\" to list/dict. Error: {error}"
    PREPARING_IMAGES_MSG = "Preparing {run_name} images..."


class UtilSystemTexts:
    COMMAND_EXE_FAIL_ERROR_MSG = "COMMAND execution FAIL: {command}"
    UNSUPPORTED_PLATFORM_ERROR_MSG = "unsupported platform: {sys_platform}, supported: {supported_os}!"
    PORT_AVAILABILITY_CHECK_ERROR_MSG = "Problem during checking port's availability."


class UtilJupyterTexts:
    IPYNB_CONVERSION_ERROR_MSG = "Py to Ipynb conversion error."


class UtilLauncherTexts:
    LOCAL_DOCKER_TUNNEL_ERROR_MSG = "Error occurred during creation of a local docker-host tunnel."
    BROWSER_STARTING_MSG = "Browser will start in few seconds. Please wait..."
    CANNOT_USE_PORT = "Cannot use required port {required_port}. Port has been set automatically to {random_port}"
    NO_WEB_BROWSER_ERROR_MSG = "Cannot find a suitable web browser - running with --no-launch option."
    PROXY_CLOSE_ERROR_MSG = "Error occurred during closing of a proxy for a {app_name}"
    WEB_APP_LAUCH_FAIL_MSG = "Failed to launch web application."
    WEB_APP_CLOSING_MSG = "Closing all connections. Please wait..."
    GO_TO_MSG = "Go to {url}"
    PROXY_CREATED_MSG = "Proxy connection created.\nPress Ctrl-C key to close a port forwarding process..."
    PROXY_CREATED_ERROR_MSG = "Error during creation of a proxy for a {app_name}."
    PROXY_CREATED_EXTENDED_ERROR_MSG = "Error occurred during creation of a proxy for a {app_name}. {reason}"
    LAUNCHING_APP_MSG = "Launching..."


class UtilHelmTexts:
    HELM_RELEASE_REMOVAL_ERROR_MSG = "Error during removal of helm release {release_name}."


class TensorboardClientTexts:
    INVALID_RUNS_ERROR_MSG = "There is no data for the following experiments: {invalid_runs_list}"
    RUNS_NOT_EXIST_ERROR_MSG = "Experiments given as parameters of the command do not exist."


class UtilDockerTexts:
    TAGS_GET_ERROR_MSG = "Error during getting list of tags for an image."
    IMAGE_DELETE_ERROR_MSG = "Error during deletion of an image."


class UtilDependenciesCheckerTexts:
    PARSE_FAIL_ERROR_MSG = "Failed to parse version({version_field}) from following input: {version_output}"
    VERSION_CMD_FAIL_MSG = "Failed to run {version_cmd} with args {version_cmd_args}. Output: {output}"
    DEPENDENCY_NOT_INSTALLED_ERROR_MSG = "{dependency_name} is not installed."
    VERSION_GET_FAIL_MSG = "Failed to get {dependency_name} version."
    INVALID_DEPENDENCY_ERROR_MSG = "{dependency_name} installed version: {installed_version}, does not match " \
                                   "expected version: {expected_version}"
    UNKNOWN_OS_ERROR_MSG = "Unknown OS version."
    GET_OS_VERSION_ERROR_MSG = "Could not determine OS version."
    UNSUPPORTED_OS_ERROR_MSG = "WARNING: This OS version ({os_name} {os_version}) is unsupported. Check the release " \
                               "notes for supported operating systems and proceed at your own risk."
    INVALID_OS_VERSION_ERROR_MSG = "WARNING: This version ({os_name} {os_version}) of the OS is not supported. Check " \
                                   "the list of supported OS in the documentation."


class UtilConfigTexts:
    USER_DIR_NOT_FOUND_ERROR_MSG = "Cannot find {user_path} directory from {config_env_name} env!"
    NCTL_CONFIG_DIR_NOT_FOUND_ERROR_MSG = "Cannot find {config_dir_name} directory in {binary_config_dir_path} " \
                                          "and {user_local_config_dir_path}. Use {config_env_name} env to point " \
                                          "{config_dir_name} directory location"


class PlatformResourcesCustomModelTexts:
    INVALID_K8S_NAME = "name must consist of lower case alphanumeric characters, '-' or '.', and must start with " \
                       "alphabetic character and end with an alphanumeric character."


class PlatformResourcesExperimentsTexts:
    REGEX_COMPILATION_FAIL_MSG = "Failed to compile regular expression: {name_filter}"
    K8S_RESPONSE_LOAD_ERROR_MSG = "preparing load of ExperimentKubernetes response object error - {err}"
    K8S_DUMP_PREPARATION_ERROR_MSG = "preparing dump of ExperimentKubernetes request object error - {err}"
    EXPERIMENT_ALREADY_EXISTS_ERROR_MSG = " experiment with name: {name} already exist!"
    EXPERIMENT_INVALID_STATE_MSG = " experiment with name: {name} already exist, " \
                                   "but it does not have any resources submitted for creation. " \
                                   "To create an experiment with the desired name," \
                                   " purge the old experiment using following command: nctl experiment cancel --purge" \
                                   " {name}"
    EXPERIMENT_UPDATE_ERROR_MSG = "Error during patching an Experiment"
    EXPERIMENT_PREV_EXP_STILL_TERMINATING = "Artfiacts of the previous experiment with the same name still exist. " \
                                            "Wait a few minutes and resubmit the experiment."


class PlatformResourcesRunsTexts:
    REGEX_COMPILATION_FAIL_MSG = "Failed to compile regular expression: {name_filter}"
    K8S_RESPONSE_LOAD_ERROR_MSG = "Preparing load of RunKubernetes response object error - {err}"
    K8S_DUMP_PREPARATION_ERROR_MSG = "Preparing dump of RunKubernetes request object error - {err}"
    RUN_UPDATE_ERROR_MSG = "Error occurred during patching a Run."


class PlatformResourcesUsersTexts:
    USERNAME_CANNOT_BE_EMPTY_ERROR_MSG = "Name of a user cannot be an empty string."
    USERNAME_TOO_LONG_ERROR_MSG = "Name of a user cannot be longer than 32 characters."
    INCORRECT_K8S_USERNAME_ERROR_MSG = "Incorrect k8s user name."
    USERNAME_IS_RESERVED_FOR_SYSTEM_USE = "Unable to create user: username is reserved or blacklisted."
    USER_PRESENCE_CHECK_ERROR_MSG = "Error occurred during checking user's presence."


class UtilKubectlTexts:
    NO_AVAILABLE_PORT_ERROR_MSG = "Available port cannot be found."
    PROXY_CREATION_OTHER_ERROR_MSG = "Other error during creation of port proxy."
    PROXY_CREATION_MISSING_PORT_ERROR_MSG = "Missing port during creation of port proxy."
    K8S_OBJECT_DELETE_ERROR_MSG = "Error occurs when deleting k8s object: {output}"
    K8S_CLUSTER_NO_CONNECTION_ERROR_MSG = "Cannot connect to K8S cluster: {output}"
    TOP_COMMAND_ERROR = "Problems during getting usage of resources."
    TOP_COMMAND_ERROR_LOG = "Incorrect format of data returned by top command: {output}"
    K8S_PORT_FORWARDING_ERROR_MSG = "Cannot forward port from K8S cluster. Check cluster configuration and " \
                                    "proxy settings."


class UtilK8sInfoTexts:
    OTHER_FIND_NAMESPACE_ERROR_MSG = "Other find_namespace error."
    NAMESPACE_DELETE_ERROR_MSG = "Error occurred during deletion of namespace {namespace}"
    CONFIG_MAP_ACCESS_ERROR_MSG = "Problem during accessing ConfigMap : {name}."
    LACK_OF_DEFAULT_TOKEN_ERROR_MSG = "Lack of default-token on a list of tokens."
    EMPTY_LIST_OF_TOKENS_ERROR_MSG = "Empty list of tokens."
    GATHERING_USERS_TOKEN_ERROR_MSG = "Problem during gathering users token."
    GATHERING_USER_CERTIFICATE_ERROR_MSG = "Problem during gathering server certificate."
    GATHERING_PASSWORD_ERROR_MSG = "Error occurred during gathering users password."
    LACK_OF_PASSWORD_ERROR_MSG = "Lack of password."
    GATHERING_EVENTS_ERROR_MSG = "Problem during gathering k8s events."
    PATCHING_CM_ERROR_MSG = "Problem during patching configmap."


class UtilK8sProxyTexts:
    PROXY_ENTER_ERROR_MSG = "k8s_proxy - enter - error"
    PROXY_EXIT_ERROR_MSG = "k8s_proxy - exit - error"
    TUNNEL_NOT_READY_ERROR_MSG = "connection on {address}:{port} NOT READY!"
    TUNNEL_ALREADY_CLOSED = "Proxy tunnel is already closed."
    K8S_PORT_FORWARDING_ERROR_MSG = "Cannot forward port from K8S cluster. Check cluster configuration and " \
                                    "proxy settings."


class CliStateTexts:
    INVALID_DEPENDENCY_ERROR_MSG = "Dependency check failed."
    KUBECTL_NAMESPACE_ERROR_MSG = "Failed to determine kubectl namespace during verification. This may occur for " \
                                  "example, due to invalid path to kubectl config, invalid k8s credentials or k8s " \
                                  "cluster being unavailable. Check your KUBECONFIG environment variable and make " \
                                  "sure that the k8s cluster is online."
    NCTL_CONFIG_NOT_SET_ERROR_MSG = "Configuration directory for nctl is not set or NCTL_CONFIG environment variable " \
                                    "points to invalid directory."
    NCTL_CONFIG_INIT_ERROR_MSG = "Config initialization failed. Reason: {exception_msg}"
    USER_NOT_ADMIN_MSG = "Only nauta administrators can run '{command_name}' command."
    USER_IS_ADMIN_MSG = "You cannot run command '{command_name}' as nauta administrator. Switch your KUBECONFIG " \
                        "environment variable to point to a valid nauta user config. If you do not have one, you " \
                        "can create it using the 'nctl user create' command."
    ADMIN_CHECK_ERROR_MSG = "Problems detected while verifying current user privileges."


class LicenseAcceptanceTexts:
    LICENSE_ACCEPTANCE_QUESTION_MSG = "DO NOT ACCESS, COPY OR PERFORM ANY PORTION OF THE PRE-RELEASE SOFTWARE " \
                                      "UNTIL YOU HAVE READ AND ACCEPTED THE TERMS AND CONDITIONS OF THIS " \
                                      "AGREEMENT LICENSE.TXT . BY COPYING, ACCESSING, OR PERFORMING " \
                                      "THE PRE-RELEASE SOFTWARE, YOU AGREE TO BE LEGALLY BOUND BY THE TERMS AND " \
                                      "CONDITIONS OF THIS AGREEMENT. Agree?"
    CANNOT_ACCEPT_LICENSE_MSG = "Cannot save license agreement - \"config\" file or directory already exists in " \
                                "{nctl_config_path}. This name is reserved for the nctl app. Remove it " \
                                "and try again."


class ConfigCmdTexts:
    HELP = "Set limits and requested resources in templates."
    HELP_C = "Number of CPUs available for training on one node. K8s format expected. Obligatory."
    HELP_M = "Amount of memory available for training on one node. K8s format expected. Obligatory."
    HELP_PN = "Name of a pack which resources' settings should be changed. If not given, command changes resources " \
              "for all packs."
    MISSING_ARGUMENTS = """Usage: nctl config [options]
Try \"nctl config -h\" for help. 
                        
Both CPU number and memory amount have to be given."""
    MISSING_CONFIG_FILE = "File with a description of a configuration is missing."
    CONFIG_FILE_INCORRECT = "File with a description of a configuration is corrupt."
    CONFIG_UPDATE = "Updating templates file with a new configuration ..."
    CPU_WRONG_FORMAT = "CPU number should be given in k8s format."
    MEMORY_WRONG_FORMAT = "Memory amount should be given in k8s format."
    ERROR_DURING_UPDATE = "Problems during updating resources."
    SUCCESS_MESSAGE = "Resources' settings have been updated with a success."
    MEMORY_SETTINGS_TOO_LOW = "Memory amount passed to the command should not be lower than {memory_value}."
    CPU_SETTINGS_TOO_LOW = "CPU number passed to the command should not be lower than {cpu_value}."


class WorkflowCmdTexts:
    HELP = "Starting, stopping, and managing workflows."


class WorkflowLogsTexts:
    SHORT_HELP = "Show logs for a given workflow."
    HELP = """
        Show logs for a given workflow.

        workflow-name - Name of workflow whose logs should be displayed.
        """
    LOCAL_PORT_OCCUPIED_ERROR_MSG = "Error occurred during creation of a proxy for elasticsearch. {exe.message}"
    PROXY_CLOSE_LOG_ERROR_MSG = "Error occurred during closing of a proxy for elasticsearch."
    PROXY_CLOSE_USER_ERROR_MSG = "Elasticsearch proxy has not been closed correctly. Check if it still exists. If " \
                                 "yes, close it manually."
    PROXY_CREATION_ERROR_MSG = "Error occurred during creation of a proxy for elasticsearch."
    OTHER_ERROR_MSG = "Failed to get workflow logs."
    NOT_FOUND_MSG = "Workflow with name {workflow_name} was not found."


class WorkflowDeleteTexts:
    SHORT_HELP = "Delete a workflow."
    HELP = """
        Deletes workflow with given name.

        name - Name of workflow which should be cancelled.
        """
    OTHER_ERROR_MSG = "Failed to delete workflow."
    NOT_FOUND_MSG = "Workflow with name {workflow_name} was not found."
    PROGRESS_MSG = "Deleting workflow {workflow_name} ..."
    SUCCESS_MSG = "Deleted workflow {workflow_name}"


class WorkflowSubmitTexts:
    SHORT_HELP = "Submit a workflow."
    HELP = """
        Creates a workflow from specification defined in file given as argument.

        workflow-path - is a path to workflow specification that will be used
        """
    LOAD_SPEC_ERROR_MSG = "Failed to load workflow definition file. Reason: {msg}"
    OTHER_ERROR_MSG = "Failed to submit workflow."
    PROGRESS_MSG = "Creating workflow ..."

class WorkflowViewTexts:
    SHORT_HELP = "Displays details of workflow with a given name."
    HELP = """
        Displays details of worfklow with a given name.

        WORKFLOW_NAME - is a name of workflow whose details should be displayed.
        """
    NOT_FOUND_MSG = "Workflow with name {workflow_name} was not found."
    OTHER_ERROR_MSG = "Failed to get workflow details."


class WorkflowListTexts:
    SHORT_HELP = "List workflows."
    NOT_FOUND_MSG = "Workflow with name {workflow_name} was not found."
    OTHER_ERROR_MSG = "Failed to get workflow details."


class TemplateCmdTexts:
    HELP = "Manage experiment templates used by the system."


class TemplateListCmdTexts:
    HELP = "Displays list of available templates - both local and remote."
    MISSING_REPOSITORY = "Repository {repository_address} does not exist or you do not have access. List below " \
                         "does not contain then any remote templates data."
    UNAUTHORIZED = "GitHub credentials are incorrect."
    OTHER_GITHUB_ERROR = "Error occurred during accessing github."
    OTHER_ERROR_DURING_ACCESSING_REMOTE_REPOSITORY = "Other error occurred during accessing remote repository."
    ERROR_DURING_LOADING_LOCAL_TEMPLATES = "Errors occurred during loading local templates. List below does not contain " \
                                           "any data of local templates."
    MISSING_CONFIGURATION_FILE = "Lack or incorrect file with configuration of model-zoo repository.  " \
                                 "Check, if the file zoo-repository.config exists in the nctl folder."
    GETTING_LIST_OF_TEMPLATES_MSG = "Getting templates list ..."
    CHECKING_PRESENCE_OF_TEMPLATE_MSG = "Checking for presence of a template ..."


class TemplateCopyCmdTexts:
    HELP = "Create a new template based on existing one."
    HELP_DESCRIPTION = "Description of a new template. If this parameter is not be provided, " \
                       " a prompt appears for the user to input the new template's description."
    HELP_VERSION = "Version of a new template. 0.1.0 version will be used by default."
    SRC_TEMPLATE_NOT_FOUND = "Source template {src_template_name} has not been found."
    TEMPLATE_ALREADY_EXISTS = "Template with name {dest_template_name} already exists."
    DESCRIPTION_PROMPT = "Enter new template description (up to {max_len} chars): "
    COPY_SUCCESS = "Template {dest_template_name} was successfully created from {src_template_name} template."
    COPY_FAILURE = "Failed to create {dest_template_name} template from {src_template_name} template."


class GithubMessages:
    GET_REQUEST_ERROR = "Error occurred during accessing github repository {url} : {http_code}"
    GET_OTHER_ERROR = "Other error during connecting github."
    MISSING_CHART_FILE = "Chart file does not exist in the checked folder."
    GET_MISSING_FILE = "File {url} does not exist."


class TemplateInstallCmdTexts(TemplateListCmdTexts):
    HELP = "Download and install template from remote repository."
    REMOTE_TEMPLATE_NOT_FOUND = "Remote template {template_name} has not been found."
    DOWNLOADING_TEMPLATE = "Installing template..."
    LOCAL_VERSION_ALREADY_INSTALLED = "Local version '{local_version}' of a '{template_name}' template is already " \
                                      "installed. Continue with replacing it with remote version '{remote_version}'?"
    FAILED_TO_LOAD_TEMPLATE = "Failed to load template {template_name}."
    FAILED_TO_INSTALL_TEMPLATE = "Failed to install template {template_name} from repository {repository_name}."



class ModelCmdTexts:
    HELP = "Manage the processing, conversion, and packaging of models."


class ModelStatusCmdTexts:
    HELP = "Displays the status of model operations."
    OTHER_ERROR_MSG = "Failed to get statuses of operations."
    HELP_U = "Name of a user to whom viewed operations belong. If not given, only operations of a current " \
             "user are considered."
    LOAD_DATA_MSG = "Loading operations' data. Please wait..."


class ModelExportCmdTexts:
    HELP = """
    Export the model using one of defined formats/list the available export formats. 
    PATH - Indicates the location of the model on the Input or Output network shares. If the 'list' value is given,
           the command displays a list of available export's formats.

    FORMAT - One of the supported formats (see nctl model export formats command). Required, if export of a model is 
            executed.

    operation-options - Options specific to a chosen format.
    """
    SHORT_HELP = "Export the model using one of defined formats/list available export formats."
    HELP_P = "Post-processing workflow used to process exported model (see nctl process-list command)."
    WRONG_EXPORT_FORMAT = "Format: {format} does not exist. Choose from: {formats}."
    WRONG_PROCESS_KIND = "Post-processing kind: {process} does not exist. Choose from: {kinds}."
    EXPORT_LIST_ERROR_MSG = "Error occurred during getting list of export's formats."
    MISSING_EXPORT_FORMAT = "Export format was not given. Choose from: {formats}."


class ModelExportLogsCmdTexts:
    SHORT_HELP = "Displays logs of a 'model export' operation."
    HELP = """
    Displays logs of an 'model export' operation.
    operation_name - Name of a 'model export' operation. The 'operation_name' argument value can be empty when the 'match' 
    option is used.
    """
    HELP_SD = "Retrieves logs produced on or after this date (ISO 8601 date format)."
    HELP_ED = "Retrieves logs produced on or before this date ( ISO 8601 date format)."
    HELP_M = "Searches for operation logs from matching values. Cannot be used with the operation_name argument."
    HELP_O = "Stores file-named operation logs."
    HELP_F = "Specifies if logs should be streamed. Streams only logs from a single operation."
    HELP_PAGER = "Display logs in interactive pager."


class ModelExportCommonTexts:
    PROXY_CREATION_ERROR_MSG = "Error during creation of a proxy for elasticsearch."
    LOGS_GET_OTHER_ERROR_MSG = "Failed to get operation logs."
    LOCAL_PORT_OCCUPIED_ERROR_MSG = "Error during creation of a proxy for elasticsearch. {exe.message}"
    PROXY_CLOSE_LOG_ERROR_MSG = "Error during closing of a proxy for elasticsearch."
    NAME_M_BOTH_GIVEN_ERROR_MSG = "Both name and -m option cannot be given. Choose one."
    NAME_M_NONE_GIVEN_ERROR_MSG = "Error: name or -m option must be given. Pass one."
    MORE_EXP_LOGS_MESSAGE = "There is more than one log to be stored. Each log will be stored in a separate file."
    OPERATION_NOT_EXISTS_ERROR_MSG = "Operation with name {operation_name} does not exist."
