export default function loadBalancer(chinaDownload, USDownload) {
  return Promise
    .race([chinaDownload, USDownload])
    .then((resolve) => resolve);
}
