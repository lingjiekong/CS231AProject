clear;
clc;
close all;

% get output from orb-slam
file_ID = fopen('CameraTrajectory.txt', 'r');
format_spec = '%f %f %f %f %f %f %f %f';
size_mat = [8 Inf];
results_file = fscanf(file_ID, format_spec, size_mat);
results_file = results_file';

% get associations file (for the timestamp)
file_ID_assoc = fopen('associations.txt', 'r');
format_spec_assoc = '%f %s %f %s';
associations_file = textscan(file_ID_assoc, format_spec_assoc);
associations_file = [num2cell(associations_file{1}) associations_file{2} num2cell(associations_file{3}) associations_file{4}];

% file to write to
write_file = 'dense_static_map.txt'; 
fid_write_file = fopen(write_file, 'w');

num_images = size(results_file,1);
scale_factor = 5000.0;
fx = 613.494812;
fy = 613.494873;
cx = 251.7;
cy = 305.02;

all_coords = zeros(0,3);

output_matrix = [];
for i = 1:1
    disp(i);
    timestamp = results_file(i);
    assoc_timestamps = associations_file(:,1);
    assoc_row = find(abs([assoc_timestamps{:}] - timestamp) < 0.0001, 1);
    rgb_filename = associations_file{assoc_row, 2};
    depth_filename = associations_file{assoc_row, 4};
    
    % To get .bin depth file
%     image_number = depth_filename(13:end-4);
%     bin_filename = [depth_bin_folder 'bin_aligned_depth_' image_number '.bin'];
%     bin_file_ID = fopen(bin_filename);
%     bin_image = fread(bin_file_ID, [640, 480], 'uint16');
%     bin_image = bin_image';
    
    rgb_image = imread(['rgbd_dataset_freiburg1_xyz/' rgb_filename]);
    depth_image = imread(['rgbd_dataset_freiburg1_xyz/' depth_filename]);
    num_rows = size(rgb_image,1);
    num_cols = size(rgb_image,2);
    
    qx = results_file(i,5);
    qy = results_file(i,6);
    qz = results_file(i,7);
    qw = results_file(i,8);
    rot_matrix = [1 - 2*qy^2 - 2*qz^2, 2*qx*qy - 2*qz*qw, 2*qx*qz + 2*qy*qw; ...
        2*qx*qy + 2*qz*qw, 1 - 2*qx^2 - 2*qz^2, 2*qy*qz - 2*qx*qw; ...
        2*qx*qz - 2*qy*qw, 2*qy*qz + 2*qx*qw, 1 - 2*qx^2 - 2*qy^2];
    trans_vec = results_file(i,2:4)';
    
    % z_values = double(bin_image) / scale_factor;
    z_values = double(depth_image) / scale_factor;
    z_values = reshape(z_values', 1, num_rows*num_cols);
    x_values = repmat(1:num_cols, 1, num_rows);
    x_values = (x_values - cx) .* z_values / fx;
    y_values = repmat(1:num_rows, num_cols, 1);
    y_values = y_values(:)';
    y_values = (y_values - cy) .* z_values / fy;
    orig_points = [x_values; y_values; z_values];
    
    trans_points = (rot_matrix * orig_points) + repmat(trans_vec, 1, size(orig_points,2));
    % trans_points = rot_matrix' * (orig_points - repmat(trans_vec, 1, size(orig_points,2)));
    valid_cols = find(orig_points(3,:));    % All transformed points where we have depth information
    trans_points_valid = trans_points(:,valid_cols);
    rgb_matrix = permute(rgb_image, [3 2 1]);
    rgb_matrix = reshape(rgb_matrix, 3, num_rows*num_cols);
    rgb_matrix_valid = double(rgb_matrix(:,valid_cols));
    write_matrix = [trans_points_valid; rgb_matrix_valid]';
    output_matrix = [output_matrix; write_matrix];
    
%     dlmwrite(write_file, write_matrix, '-append', 'delimiter', ' ');    % Write XYZRGB information to file
end

% 3D scatter plot in matlab

% figure(1)
% x = output_matrix(:,1);
% y = output_matrix(:,2);
% z = output_matrix(:,3);
% s = ones(size(x));
% rgb = output_matrix(:,4:6)/256;
% scatter3(x,y,z,s,rgb)
% xlabel('x')
% ylabel('y')
% zlabel('z')



    