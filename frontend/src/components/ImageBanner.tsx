import React from 'react';

interface ImageBannerProps {
    imageUrl: string;
}

const ImageBanner: React.FC<ImageBannerProps> = ({ imageUrl }) => {
    return (
        <div className='imageBanner'>
            <img src={imageUrl} alt='banner'/>
            <div className='textOverlay'>Kingsmen HYC Project</div>
        </div>
    );
};

export default ImageBanner;